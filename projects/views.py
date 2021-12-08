from django.shortcuts import redirect, render
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
    )
from django.contrib import messages
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView
)
from django.http import JsonResponse
from django.views.generic.base import View
from accounts.models import User
from projects import models
import json
from django.core.serializers import serialize
from projects.forms import ProjectForm
# Create your views here.

class ProjectListView(LoginRequiredMixin, ListView):
    context_object_name = 'projects'
    template_name = 'projects/list.html'

    def get_queryset(self):
        return models.Project.objects.filter(author=self.request.user)

class ProjectCreateView(LoginRequiredMixin, CreateView):
    form_class = ProjectForm
    template_name = 'projects/new.html'

    def form_valid(self, form):
        project = form.save(commit=False)
        project.author = self.request.user
        project.save()
        return redirect('projects:project_detail', project.slug)

class ProjectDetailView(LoginRequiredMixin, UserPassesTestMixin, View):
    template_name = 'projects/detail.html'

    def get_project(self):
        return models.Project.objects.get(slug=self.kwargs['slug'])
    
    def get_labels(self):
        labels = models.IssueLabel.objects.filter(project=self.get_project())
        return labels


    def get(self, request, *args, **kwargs):
        labels = self.get_labels()
        if request.is_ajax():
            data = {}
            data['labels'] = serialize('json', queryset=labels)
            return JsonResponse(data)

        context = {
            'project':self.get_project(),
            'labels' : labels,
        }
        return render(request, self.template_name, context)
    
    def test_func(self):
        if self.get_project().author == self.request.user:
            return True
        return False
    
    def handle_no_permission(self):
        messages.success(self.request, 'You have no permission to view this page')
        return redirect('base:dashboard')

class ProjectSettingsView(LoginRequiredMixin, UserPassesTestMixin, View):
    template_name = 'projects/settings.html'

    def get_project(self):
        return models.Project.objects.get(slug=self.kwargs['slug'])

    def get(self, request, *args, **kwargs):
        project = self.get_project()
        projectForm = ProjectForm(instance=project)
        context = {
            'project':project,
            'projectForm':projectForm
        }
        return render(request, self.template_name, context)

    def test_func(self):
        if self.get_project().author == self.request.user:
            return True
        return False
    
    def handle_no_permission(self):
        messages.success(self.request, 'You have no permission to view this page')
        return redirect('base:dashboard')


class ProjectEditView(LoginRequiredMixin, UserPassesTestMixin, View):
    template_name = 'projects/new.html'

    def get_project(self):
        return models.Project.objects.get(slug=self.kwargs['slug'])

    def post(self, request, *args, **kwargs):
        form = ProjectForm(request.POST, instance=self.get_project())
        if form.is_valid:
            form.save()
            messages.success(self.request, 'Project Updated successfully')
            return redirect('projects:project_detail', self.get_project().slug)

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
        return redirect('projects:project_list')

    def test_func(self):
        if self.get_project().author == self.request.user:
            return True
        return False
    
    def handle_no_permission(self):
        messages.success(self.request, 'You have no permission to view this page')
        return redirect('base:dashboard')


def assign_task(request):
    if request.is_ajax():
        user = None
        if request.GET.get('email') != '':
            email = request.GET.get('email')
            user = User.objects.get(email=email)
        slug = request.GET.get('task')
        task = models.Issue.objects.get(slug=slug)
        
        task.assigned_to = user if user else None
        task.save()
        data = {}
        data['message'] = 'Hurray! 🎈'
        return JsonResponse(data)
    return redirect('project:project_list')

    


