from django.contrib import admin
from traineesubject.admin.model_admin_mixins import CrfModelAdminMixin
from traineesubject.forms.education_questionaire_form import EducationQuestionaireForm
from traineesubject.models.educational_questionaire import EducationalQuestionaire
from ..admin_site import traineesubject_admin


@admin.register(EducationalQuestionaire, site=traineesubject_admin)
class EducationQuestionaireAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = EducationQuestionaireForm
    fields = (
        "subject_visit",
        "working",
        "work_type",
        "occupation",
        "salary")
    radio_fields = {
        "working": admin.VERTICAL,
        "work_type": admin.VERTICAL,
        "occupation": admin.VERTICAL,
        "salary": admin.VERTICAL}