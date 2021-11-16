from django import forms
from projects.models import Project
from bugtail.helpers.form_helper import add_form_control

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['author', 'slug']
    
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        add_form_control(self)