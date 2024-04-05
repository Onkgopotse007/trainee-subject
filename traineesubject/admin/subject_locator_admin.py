from django.conf import settings
from django.contrib import admin
from django.urls.base import reverse
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_base.modeladmin_mixins import audit_fieldset_tuple
from edc_locator.fieldsets import work_contacts_fieldset
from edc_model_admin import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin,
    ModelAdminReadOnlyMixin, ModelAdminInstitutionMixin,
    ModelAdminRedirectOnDeleteMixin)
from .exportaction_mixin import ExportActionMixin
from edc_subject_dashboard import ModelAdminSubjectDashboardMixin
from traineesubject.forms.subject_locator_form import SubjectLocatorForm

from traineesubject.models.subject_locator import SubjectLocator
from ..admin_site import traineesubject_admin
from ..fieldsets import (subject_contacts_fieldset,indirect_contacts_fieldset,
                         other_indirect_contacts_fieldset)


class ModelAdminMixin(
        ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
        ModelAdminFormAutoNumberMixin, ModelAdminRevisionMixin,
        ModelAdminAuditFieldsMixin, ModelAdminReadOnlyMixin,
        ModelAdminInstitutionMixin, ModelAdminRedirectOnDeleteMixin,
        ModelAdminSubjectDashboardMixin,ExportActionMixin):

    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'
    subject_dashboard_url = 'subject_dashboard_url'

    post_url_on_delete_name = settings.DASHBOARD_URL_NAMES.get(
        subject_dashboard_url)

    def post_url_on_delete_kwargs(self, request, obj):
        return dict(subject_identifier=obj.subject_identifier)

    def redirect_url(self, request, obj, post_url_continue=None):
        if obj:
            return reverse(settings.DASHBOARD_URL_NAMES.get(
                self.subject_dashboard_url),
                kwargs=dict(subject_identifier=obj.subject_identifier))
        else:
            return super().redirect_url(request, obj, post_url_continue)
        
@admin.register(SubjectLocator, site=traineesubject_admin)
class SubjectLocatorAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = SubjectLocatorForm

    fieldsets = (
        (None, {
            'fields': (
                'subject_identifier',
                'date_signed',
                'local_clinic',
                'home_village',
            )}),
        subject_contacts_fieldset,
        work_contacts_fieldset,
        indirect_contacts_fieldset,
        other_indirect_contacts_fieldset,
        audit_fieldset_tuple,
    )

    radio_fields = {
        'may_visit_home': admin.VERTICAL,
        'may_call': admin.VERTICAL,
        'may_sms': admin.VERTICAL,
        'may_call_work': admin.VERTICAL,
        'may_contact_indirectly': admin.VERTICAL,
        'has_alt_contact': admin.VERTICAL, }

    list_filter = (
        'may_visit_home',
        'may_call',
        'may_sms',
        'may_call_work',
        'may_contact_indirectly')

    list_display = (
        'subject_identifier',
        'dashboard',
        'visit_home',
        'call',
        'sms',
        'call_work',
        'contact_indirectly')

    search_fields = ('subject_identifier',)

