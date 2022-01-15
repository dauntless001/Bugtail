from projects.models import Project
from django.db.models import Q


def get_user_projects(user):
    collaborators_list = []
    collaborators_list.append(user)
    projects = Project.objects.filter(
        Q(author=user)|
        Q(collaborators__in=collaborators_list))
    return projects