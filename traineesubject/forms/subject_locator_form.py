from django import forms
from edc_form_validators import FormValidatorMixin

from ..models import subject_locator


class SubjectLocatorForm(FormValidatorMixin, forms.ModelForm):


    subject_identifier = forms.CharField(
        label='Subject Identifier',
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = subject_locator.SubjectLocator
        fields = '__all__'