from django import template
from django.template.defaultfilters import stringfilter
from bugtail.helpers.project_helper import get_user_projects
from projects.models import IssueLabel, Project

register = template.Library()

@register.inclusion_tag('partials/_sidebar.html')
def fetch_projects(user):
    print(user, 'userererere')
    return ['ab', 'acc']#{'projects':get_user_projects(user)}

@register.simple_tag
def fetch_label_tasks(project, label):
    issues = Project.objects.get(slug=project).issue_set.filter(label__short_name=label)
    return issues
    
