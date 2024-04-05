from django import forms
from edc_base.sites import SiteModelFormMixin

from ..models import SubjectRequisitionResult


class SubjectRequisitionResultForm(SiteModelFormMixin,forms.ModelForm):

    class Meta:
        model = SubjectRequisitionResult
        fields ='__all__'

