from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from bugtail.helpers.project_helper import get_user_projects
# Create your views here.

class DashboardView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        projects = get_user_projects(self.request.user)[:8]
        context = {
            'projects':projects,
            'view_all': True if projects.count() > 8 else False
        }
        return render(request, 'index.html', context)

def error_404(request, exception):
    return render(request, '404.html')

def error_500(request, *args, **kwargs):
    return render(request, '500.html')