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
from comments.forms import CommentForm
from projects import models
import json
from django.core.serializers import serialize
from projects.forms import IssueForm, ProjectForm
from collaborators.models import CollaborationRequest
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
            'form': IssueForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            ajaxData = request.POST
            label = models.IssueLabel.objects.get(project__slug=self.kwargs['slug'],
                short_name=ajaxData['to'])
            print(label)
            issue = models.Issue.objects.get(slug=ajaxData['slug'])
            issue.label = label
            issue.save()
            data = {}
            data['message'] = 'Successful'
            return JsonResponse(data)
    
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
        data['message'] = f'Task Assigned 🎈 to {user}' if user else f'Task Unassigned'
        data['messageType'] = 'success'
        return JsonResponse(data)
    return redirect('project:project_list')

class AddRemoveCollaboratorView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            ajaxData = request.GET
            data = {}
            project = models.Project.objects.get(slug=self.kwargs['slug'])
            user = User.objects.get(email=ajaxData['email'])
            project.collaborators.remove(user)
            data['message'] = f'Collaborator with email {ajaxData["email"]} has been removed'
            data['messageType'] = 'success'
            return JsonResponse(data, safe=False)
    def post(self, request, *args, **kwargs):
        
        if request.is_ajax():
            data = {}
            ajaxData = request.POST
            project = models.Project.objects.get(slug=self.kwargs['slug'])
            #Check if user exists
            try:
                user = User.objects.get(email=ajaxData['email'])
                if project.collaborators.filter(email=user.email).exists():
                    data['message'] = 'User with email '+ ajaxData['email'] +' is already a collaborator on '+ project.name
                    data['messageType'] = 'info'
                else:
                    project.collaborators.add(user)
                    data['message'] = 'Collaborator with email:'+ ajaxData['email']+' has been added'
                    data['messageType'] = 'success'
            except:
                data['message'] = 'User with email '+ ajaxData['email'] +' Appears not to Exist, Please Check Email and try Again'
                data['messageType'] = 'error'
            return JsonResponse(data, safe=False)


class CreateIssueView(LoginRequiredMixin,UserPassesTestMixin,View):
    def get_project(self):
        return models.Project.objects.get(slug=self.kwargs['slug'])
    
    def post(self, request, *args, **kwargs):
        label = models.IssueLabel.objects.get(project=self.get_project(), short_name='open')
        ajaxData = request.POST
        data = {}
        if ajaxData['label']:
            label = models.IssueLabel.objects.get(project=self.get_project(), short_name=ajaxData['label'])
        issue = {
            'project':self.get_project(),
            'name' : ajaxData['title'],
            'desc' : ajaxData['desc'],
            'priority': ajaxData['priority'],
            'label': label

        }
        models.Issue.objects.create(**issue)
        data['message'] = 'Issue Created Successfully'
        data['messageType'] = 'success'
        return JsonResponse(data, safe=False)
        

    def test_func(self):
        user = self.request.user
        if  user == self.get_project().author or user in self.get_project().collaborators.all():
            return True
        return False
    
    def handle_no_permission(self):
        messages.success(self.request, 'You can\'t add issues in this project')
        return redirect('base:dashboard')


class IssueView(LoginRequiredMixin,UserPassesTestMixin, View):
    template_name = 'issues/detail.html'

    def get_project(self):
        return models.Project.objects.get(slug=self.kwargs['slug'])
    
    def get_issue(self):
        return models.Issue.objects.get(project__slug=self.get_project().slug, slug=self.kwargs['issue_slug'])
    
    def get(self, request, *args, **kwargs):
        commentForm = CommentForm()
        context = {
            'issue':self.get_issue(),
            'commentForm' : commentForm,
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwrgs):
        commentForm = CommentForm(request.POST)
        comment = commentForm.save(commit=False)
        comment.author, comment.issue = self.request.user, self.get_issue()
        comment.save()
        messages.success(request, 'Comment Uploaded successfully')
        return redirect('projects:issue_detail', self.get_issue().project.slug,self.get_issue().slug)
        # if request.is_ajax():
        #     data = {}
        #     data['message'] = 'Success'
        #     return JsonResponse(data, safe=False)


    def test_func(self):
        user = self.request.user
        if  user == self.get_project().author or user in self.get_project().collaborators.all():
            return True
        return False
    
    def handle_no_permission(self):
        messages.success(self.request, 'You can\'t view issue in this project')
        return redirect('base:dashboard')