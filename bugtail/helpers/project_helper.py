from projects.models import Project


def get_user_projects(user):
    projects = Project.objects.filter(author=user)
    return projects