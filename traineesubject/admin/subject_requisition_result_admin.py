from django.contrib import admin
from edc_senaite_interface.admin import SenaiteResultAdminMixin
from ..admin_site import traineesubject_admin
from ..forms import SubjectRequisitionResultForm
from ..models import SubjectRequisitionResult
from .exportaction_mixin import ExportActionMixin


@admin.register(SubjectRequisitionResult,site=traineesubject_admin)
class SubjectRequisitionResultAdmin(SenaiteResultAdminMixin,admin.ModelAdmin,ExportActionMixin):
    
    form = SubjectRequisitionResultForm