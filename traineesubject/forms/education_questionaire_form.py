from django import forms
from traineesubject.models.educational_questionaire import EducationalQuestionaire
from .forms_mixin import SubjectModelFormMixin
from edc_form_validators import FormValidatorMixin
from trainee_validations.form_validators import EducationQuestionaireValidationForm


class EducationQuestionaireForm(SubjectModelFormMixin, forms.ModelForm):
    form_validator_cls = EducationQuestionaireValidationForm

    class Meta:
        model = EducationalQuestionaire
        fields = '__all__'
