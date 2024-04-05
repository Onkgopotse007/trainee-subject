from django.contrib import admin
from traineesubject.models.subject_screening import SubjectScreening
from ..forms  import subject_screening_form
from ..admin_site import traineesubject_admin
from edc_base.sites.admin import ModelAdminSiteMixin
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_model_admin import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin,
    ModelAdminReadOnlyMixin, ModelAdminInstitutionMixin,
    ModelAdminRedirectOnDeleteMixin)
from edc_metadata import NextFormGetter
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fields, audit_fieldset_tuple)
from .exportaction_mixin import ExportActionMixin

class ModelAdminMixin(ModelAdminNextUrlRedirectMixin,
                      ModelAdminFormInstructionsMixin,
                      ModelAdminFormAutoNumberMixin, ModelAdminRevisionMixin,
                      ModelAdminAuditFieldsMixin, ModelAdminReadOnlyMixin,
                      ModelAdminInstitutionMixin,
                      ModelAdminRedirectOnDeleteMixin,
                      ModelAdminSiteMixin,ExportActionMixin):
                      
    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'
    next_form_getter_cls = NextFormGetter


@admin.register(SubjectScreening,site=traineesubject_admin)
class SubjectScreeningAdmin( ModelAdminMixin, admin.ModelAdmin):
    readonly_fields = ('screening_identifier',)
    form = subject_screening_form.SubjectScreeningForm

    fieldsets = (
        (None, {
            'fields': (
                'screening_identifier',
                'enrollment_interest',
                'disinterest_reason',
                'disinterest_reason_other',
                'citizen',
                'legal_marriage',
                'marriage_certificate',
                'marriage_certificate_no',
                'is_minor',
                'guardian',
                'literate',
                'literate_witness',
                'enrollment_site',
                'enrollment_site_other'
            )}),
            audit_fieldset_tuple)
    search_fields = ('subject_identifier',)

    radio_fields = {
        "citizen":admin.VERTICAL,
        "legal_marriage":admin.VERTICAL,
        "marriage_certificate":admin.VERTICAL,
        "enrollment_interest":admin.VERTICAL,
        'is_minor': admin.VERTICAL,
        'guardian': admin.VERTICAL,
        "literate":admin.VERTICAL,
        "literate_witness":admin.VERTICAL,
        "disinterest_reason":admin.VERTICAL,}

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj=obj)
                + audit_fields)