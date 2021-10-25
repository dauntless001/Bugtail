from django import template
from django.template.defaultfilters import stringfilter
from bugtail.helpers.project_helper import get_user_projects

register = template.Library()

@register.inclusion_tag('partials/_sidebar.html')
def fetch_projects(user):
    print(user, 'userererere')
    return ['ab', 'acc']#{'projects':get_user_projects(user)}
