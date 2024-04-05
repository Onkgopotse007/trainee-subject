from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple
from traineesubject.forms.offschedule_form import OffScheduleForm
from traineesubject.models.offschedule import OffSchedule
from ..admin_site import traineesubject_admin
from .model_admin_mixins import ModelAdminMixin


@admin.register(OffSchedule, site=traineesubject_admin)
class OffScheduleAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = OffScheduleForm

    fieldsets = (
        (None, {
            'fields': [
                'schedule_name',
                'subject_identifier'
            ]}
         ), audit_fieldset_tuple)

    list_filter = ('schedule_name', 'subject_identifier',)