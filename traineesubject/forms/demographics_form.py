from django import forms
from traineesubject.models.demographics import Demographic
from .forms_mixin import SubjectModelFormMixin
from trainee_validations.form_validators import DemographicValidationForm


class DemographicForm(SubjectModelFormMixin,forms.ModelForm):
    form_validator_cls = DemographicValidationForm

    class Meta:
        model = Demographic
        fields = '__all__'