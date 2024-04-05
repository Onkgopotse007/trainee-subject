from django import forms
from django.conf import settings
from edc_base.sites import SiteModelFormMixin
from edc_consent.modelform_mixins import ConsentModelFormMixin
from edc_form_validators import FormValidatorMixin
from traineesubject.choices import IDENTITY_TYPE
from traineesubject.forms.forms_mixin import SubjectModelFormMixin
from edc_form_validators import FormValidatorMixin
from traineesubject.models.subject_consent import SubjectConsent
from trainee_validations.form_validators import SubjectConsentFormValidator


class SubjectConsentForm(SubjectModelFormMixin, ConsentModelFormMixin):

    form_validator_cls = SubjectConsentFormValidator

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    identity_type = forms.CharField(
        label='What type of identity number is this?',
        widget=forms.RadioSelect(choices=list(IDENTITY_TYPE)))

    class Meta:
        model = SubjectConsent
        fields = '__all__'