from django import forms
from django.apps import apps as django_apps
from edc_base.sites import SiteModelFormMixin
from edc_constants.constants import OTHER, ALIVE, UNKNOWN, DEAD
from edc_form_validators import FormValidatorMixin
from edc_form_validators.base_form_validator import INVALID_ERROR
from edc_visit_tracking.form_validators import (VisitFormValidator as BaseVisitFormValidator)
from edc_appointment.constants import IN_PROGRESS_APPT

from ..models import subject_visit


class VisitFormValidator(BaseVisitFormValidator):

    @property
    def appointment_cls(self):
        return django_apps.get_model('edc_appointment.appointment')

    def validate_visit_code_sequence_and_reason(self):
        appointment = self.cleaned_data.get('appointment')
        reason = self.cleaned_data.get('reason')
        if appointment:
            if appointment.visit_code_sequence == 0:

                reasons = ['missed_visit', 'fu_visit/contact']

                if(appointment.visit_code == '1000T' and reason in reasons):
                    raise forms.ValidationError(
                        {'reason': 'Invalid visit reason'},
                        code=INVALID_ERROR)
                if reason == 'unscheduled_visit/contact':
                    raise forms.ValidationError(
                        {'reason': 'This can not be an unscheduled visit/contact.'})
            else:
                if reason == 'initial_visit/contact':
                    raise forms.ValidationError({
                        'reason': 'This can not be an initial visit/contact.'})

        in_progress_count = self.appointment_cls.objects.filter(
            subject_identifier=appointment.subject_identifier,
            appt_status=IN_PROGRESS_APPT).count()

        if in_progress_count > 1:
            raise forms.ValidationError(
                'There is more than one appointment in progress. Cannot proceed.')

    def validate_required_fields(self):

        self.required_if(
            'unscheduled_visit/contact',
            field='reason',
            field_required='reason_unscheduled')

        self.required_if(
            OTHER,
            field='info_source',
            field_required='info_source_other')

        self.required_if(
            OTHER,
            field='reason_unscheduled',
            field_required='reason_unscheduled_other')

    def validate_presence(self):
        """Raise an exception if 'is_present' does not make sense relative to
         'survival status', 'reason' and 'info_source'."""
        cleaned_data = self.cleaned_data

        if (self.cleaned_data.get('reason') == 'death' and cleaned_data.get(
                'info_source') in ['clinic_visit', 'other_contact_subject']):
                raise forms.ValidationError(
                    {'info_source': 'Source of information cannot be from '
                     'participant if visit reason is \'Death\'.'})

    def validate_survival_status_if_alive(self):
        if (self.cleaned_data.get('reason') == 'death' and self.cleaned_data.get(
                'survival_status') in [ALIVE, UNKNOWN]):
            raise forms.ValidationError(
                {'survival_status': ('Visit reason is death, survival '
                                     'status must be \'Deceased\'')})

        if (self.cleaned_data.get('survival_status') == DEAD and
                not self.cleaned_data.get('reason') == 'death'):
            raise forms.ValidationError(
                {'reason': 'Survival status is deceased, visit reason must be death.'})


class SubjectVisitForm (
        SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):

    form_validator_cls = VisitFormValidator

    class Meta:
        model = subject_visit.SubjectVisit
        fields = '__all__'
