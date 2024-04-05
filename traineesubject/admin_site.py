from django.contrib.admin import AdminSite as DjangoAdminSite
from django.contrib.sites.shortcuts import get_current_site


class AdminSite(DjangoAdminSite):
    site_title="Trainee"
    site_url ='/administration/'
    enable_nav_sidebar = False
    site_header = "Trainee+ EDC"

    def each_context(self,request):
        context = super().each_context(request)
        context.update(global_site=get_current_site(request))
        label = f'Trainee+ {get_current_site(request).name.title()}: Subjects'
        context.update(
            site_title =label,
            site_header = label,
            index_title =label,
        )

        return context
    
traineesubject_admin = AdminSite(name="traineesubject_admin")