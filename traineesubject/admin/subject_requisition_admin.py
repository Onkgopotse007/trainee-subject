
from django.contrib import admin
from edc_lab.admin import RequisitionAdminMixin
from edc_lab.admin import requisition_verify_fields
from edc_lab.admin import requisition_verify_fieldset, requisition_status_fieldset
from edc_model_admin import audit_fieldset_tuple
from edc_senaite_interface.admin import SenaiteRequisitionAdminMixin
from traineesubject.admin.model_admin_mixins import CrfModelAdminMixin
from traineesubject.forms.subject_requisition_form import SubjectRequisitionForm
from traineesubject.models.subject_requisition import SubjectRequisition
from ..admin_site import traineesubject_admin


requisition_identifier_fields = (
    'requisition_identifier',
    'identifier_prefix',
    'primary_aliquot_identifier',
)

requisition_identifier_fieldset = (
    'Identifiers', {
        'classes': ('collapse',),
        'fields': (requisition_identifier_fields)})





@admin.register(SubjectRequisition, site=traineesubject_admin)
class SubjectRequisitionAdmin( CrfModelAdminMixin,RequisitionAdminMixin,
                                SenaiteRequisitionAdminMixin,admin.ModelAdmin):

    form = SubjectRequisitionForm
    ordering = ('requisition_identifier',)

    fieldsets = (
        (None, {
            'fields': (
                'subject_visit',
                'requisition_datetime',
                'is_drawn',
                'reason_not_drawn',
                'reason_not_drawn_other',
                'drawn_datetime',
                'study_site',
                'panel',
                'item_type',
                'item_count',
                'estimated_volume',
                'priority',
                'exists_on_lis',
                'sample_id',
                'comments',
            )}),
        requisition_status_fieldset,
        requisition_identifier_fieldset,
        requisition_verify_fieldset,
        audit_fieldset_tuple)

    radio_fields = {
        'is_drawn': admin.VERTICAL,
        'reason_not_drawn': admin.VERTICAL,
        'item_type': admin.VERTICAL,
        'priority': admin.VERTICAL,
        'study_site': admin.VERTICAL,
        'exists_on_lis': admin.VERTICAL,
    }

    list_display = ('subject_visit', 'is_drawn', 'panel', 'estimated_volume',)

    def get_readonly_fields(self, request, obj=None):
        on_lis = getattr(obj, 'sample_id', None)
        read_only = (super().get_readonly_fields(request, obj)
                     + requisition_identifier_fields
                     + requisition_verify_fields)
        return read_only + ('exists_on_lis', 'sample_id', ) if on_lis else read_only

    def get_previous_instance(self, request, instance=None, **kwargs):
        """Returns a model instance that is the first occurrence of a previous
        instance relative to this object's appointment.
        """
        obj = None
        appointment = instance or self.get_instance(request)

        if appointment:
            while appointment:
                options = {
                    '{}__appointment'.format(self.model.visit_model_attr()):
                        self.get_previous_appt_instance(appointment)
                    }
                obj = self.model.objects.filter(**options).first()
                appointment = self.get_previous_appt_instance(appointment)
        return obj
