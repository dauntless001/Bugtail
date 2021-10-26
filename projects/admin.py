from django.contrib import admin
from projects.models import Issue,IssueLabel, Project
# Register your models here.
admin.site.register(Issue)
admin.site.register(IssueLabel)
admin.site.register(Project)
