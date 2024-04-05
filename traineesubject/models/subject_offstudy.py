from edc_base.model_mixins import BaseUuidModel
from django.db import models
from edc_constants.choices import YES_NO
from edc_base.utils import get_utcnow
from edc_protocol.validators import (
    date_not_before_study_start, datetime_not_before_study_start)
from edc_base.model_validators import date_not_future, datetime_not_future
from ..choices import REASON_FOR_EXIT
from edc_base.model_fields import OtherCharField
from edc_base.model_managers import HistoricalRecords
from edc_identifier.managers import SubjectIdentifierManager
from edc_consent.model_mixins import RequiresConsentFieldsModelMixin

class SubjectOffStudy(RequiresConsentFieldsModelMixin,BaseUuidModel):

    #action_name = SUBJECT_OFFSTUDY_ACTION

    tracking_identifier_prefix = 'SO'

    subject_identifier = models.CharField(
        max_length=50,
        unique=True)

    schedule = models.CharField(
        verbose_name='Are scheduled data being submitted on the exit date?',
        max_length=3,
        choices=YES_NO,)

    offstudy_date = models.DateField(
        verbose_name='Offstudy date',
        null=True,
        default=get_utcnow,
        validators=[date_not_before_study_start, date_not_future],)

    report_datetime = models.DateTimeField(
        verbose_name='Report datetime',
        validators=[datetime_not_before_study_start, datetime_not_future],
        null=True,
        default=get_utcnow,)

    reason = models.CharField(
        verbose_name='Reason for exit',
        max_length=50,
        choices=REASON_FOR_EXIT,
        null=True,)

    reason_other = OtherCharField()


    def natural_key(self):
        return (self.subject_identifier)

    natural_key.dependencies = ['sites.Site']

    objects = SubjectIdentifierManager()

    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        self.consent_version = None
        super().save(*args, **kwargs)

    class Meta:
        app_label = 'trainee_subject'
        verbose_name = 'Subject off Study'
        verbose_name_plural = 'Subject Off Study'