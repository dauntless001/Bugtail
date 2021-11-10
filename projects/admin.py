from django.contrib import admin
from projects.models import Issue,IssueLabel, Project, ProjectIssueLabel
# Register your models here.
admin.site.register(Issue)
admin.site.register(IssueLabel)
admin.site.register(Project)
admin.site.register(ProjectIssueLabel)
