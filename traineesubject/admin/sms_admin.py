from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple
from traineesubject.forms.sms_form import SMSForm

from traineesubject.models.sms import SMS

from ..admin_site import traineesubject_admin

from .model_admin_mixins import ModelAdminMixin


@admin.register(SMS, site=traineesubject_admin)
class SMSAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = SMSForm

    fieldsets = (
        (None, {
            'fields': ('subject_identifier',
                       'date_time_form_filled',
                       'next_ap_date',
                       'date_reminder_sent',
                       'sms_outcome'),
        }), audit_fieldset_tuple)

    radio_fields = {'sms_outcome': admin.VERTICAL}

    list_display = ('date_time_form_filled', 'next_ap_date',
                    'date_reminder_sent', 'sms_outcome')