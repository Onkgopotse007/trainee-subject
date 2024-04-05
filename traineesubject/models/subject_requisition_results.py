from django.db import models
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_base.model_mixins import BaseUuidModel

from simple_history.models import HistoricalRecords
from edc_senaite_interface.model_mixins import SenaiteResultModelMixin, SenaiteResultValueMixin


class SubjectRequisitionResult(SenaiteResultModelMixin, SiteModelMixin, BaseUuidModel):

    requisition_model = 'traineesubject.subjectrequisition'

    history = HistoricalRecords()

    class Meta:
        app_label = 'traineesubject'
        verbose_name = 'Sample Result'


class SubjectResultValue(SenaiteResultValueMixin, BaseUuidModel):

    result = models.ForeignKey(SubjectRequisitionResult, on_delete=models.PROTECT)

    history = HistoricalRecords()

    class Meta:
        app_label = 'traineesubject'
        verbose_name = 'Analysis Result Value'