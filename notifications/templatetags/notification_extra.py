from django import template
from django.template.defaultfilters import stringfilter
from bugtail.helpers.project_helper import get_user_projects
from notifications.models import Notification

register = template.Library()

@register.inclusion_tag('partials/_sidebar.html')
def fetch_projects(user):
    print(user, 'userererere')
    return ['ab', 'acc']#{'projects':get_user_projects(user)}

@register.simple_tag
def unread_notifications(user):
    notifications = Notification.objects.filter(author=user, read=False)[:5]
    return notifications