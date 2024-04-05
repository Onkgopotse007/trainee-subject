from django.contrib import admin
from traineesubject.admin.model_admin_mixins import CrfModelAdminMixin
from traineesubject.forms.community_engagement_form import CommunityEngagementForm
from traineesubject.models.community_engagement import CommunityEngagement
from ..admin_site import traineesubject_admin


@admin.register(CommunityEngagement, site=traineesubject_admin)
class CommunityEngagementAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = CommunityEngagementForm
    fields = (
        "subject_visit",
        "community_activity",
        "voting_status",
        "major_problems",
        "problem_solving")
    radio_fields = {
        "community_activity": admin.VERTICAL,
        "voting_status": admin.VERTICAL,
        "major_problems": admin.VERTICAL,
        "problem_solving": admin.VERTICAL}