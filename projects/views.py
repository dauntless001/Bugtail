from django.shortcuts import redirect, render
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
    )
from django.contrib import messages
from django.views.generic import (
    ListView,
)
from django.views.generic.base import View
from projects import models

# Create your views here.

class ProjectListView(LoginRequiredMixin, ListView):
    context_object_name = 'projects'
    template_name = 'projects/list.html'

    def get_queryset(self):
        return models.Project.objects.filter(author=self.request.user)


class ProjectDetailView(LoginRequiredMixin, UserPassesTestMixin, View):
    template_name = 'projects/detail.html'

    def get_project(self):
        return models.Project.objects.get(slug=self.kwargs['slug'])

    def get(self, request, *args, **kwargs):
        context = {
            'project':self.get_project(),
        }
        return render(request, self.template_name, context)
    
    def test_func(self):
        if self.get_project().author == self.request.user:
            return True
        return False
    
    def handle_no_permission(self):
        messages.success(self.request, 'You have no permission to view this page')
        return redirect('base:dashboard')



class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, View):
    template_name = 'projects/detail.html'

    def get_project(self):
        return models.Project.objects.get(slug=self.kwargs['slug'])

    def get(self, request, *args, **kwargs):
        try:
            project = self.get_project()
            project.delete()
            messages.success(self.request, 'Project deleted successfully')
        except models.Project.DoesNotExist:
            messages.success(self.request, 'This project seems to not exist')
        return redirect('base:dashboard')

    def test_func(self):
        if self.get_project().author == self.request.user:
            return True
        return False
    
    def handle_no_permission(self):
        messages.success(self.request, 'You have no permission to view this page')
        return redirect('base:dashboard')

    


