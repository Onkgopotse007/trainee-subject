from django.db import models
from django import forms
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import CurrentSiteManager
from edc_consent.model_mixins import RequiresConsentFieldsModelMixin
from edc_identifier.managers import SubjectIdentifierManager
from edc_visit_schedule.model_mixins import OffScheduleModelMixin
from django.apps import apps as django_apps


class OffSchedule(OffScheduleModelMixin, BaseUuidModel):
    
    subject_identifier = models.CharField(
        verbose_name="Subject Identifier",
        max_length=50)

    schedule_name = models.CharField(max_length=25,
                                     blank=True,
                                     null=True)

    community_arm = models.CharField(max_length=25,
                                     blank=True,
                                     null=True)

    onsite = CurrentSiteManager()

    objects = SubjectIdentifierManager()

    history = HistoricalRecords()

    def take_off_schedule(self):
        pass


    @property
    def latest_consent_obj_version(self):

        subject_consent_cls = django_apps.get_model('traineesubject.subjectconsent')

        subject_consents = subject_consent_cls.objects.filter(
             subject_identifier=self.subject_identifier,)
        if subject_consents:
            latest_consent = subject_consents.latest('consent_datetime')
            return latest_consent.version
        else:
            raise forms.ValidationError('Missing Subject Consent form, cannot proceed.')


    def save(self, *args, **kwargs):
        self.consent_version = None
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('subject_identifier', 'schedule_name')