from django import forms
from projects.models import Issue, Project
from bugtail.helpers.form_helper import add_form_control


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['author', 'slug']
    
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        add_form_control(self)

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        exclude = ['project', 'slug', 'label']
    
    def __init__(self, *args, **kwargs):
        super(IssueForm, self).__init__(*args, **kwargs)
        add_form_control(self)