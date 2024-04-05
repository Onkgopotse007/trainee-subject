from django.contrib import admin
from traineesubject.admin.model_admin_mixins import CrfModelAdminMixin
from traineesubject.forms.demographics_form import DemographicForm
from traineesubject.models.demographics import Demographic
from ..admin_site import traineesubject_admin


@admin.register(Demographic, site=traineesubject_admin)
class DemographicAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = DemographicForm
    fields = (
        "subject_visit",
        "marital_status",
        "women_number_husbands",
        "men_number_wives",
        "housemate")
    radio_fields = {
        "marital_status": admin.VERTICAL,
        "housemate": admin.VERTICAL}