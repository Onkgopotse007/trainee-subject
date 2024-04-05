from django.apps import apps as django_apps
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from ..choices import ENROLLMENT_SITES


class FacilityListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Facility')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'facility'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return ENROLLMENT_SITES
    
    def queryset(self,request,queryset):
        name = "What to do here"