from django.db import models
from bugtail.helpers import model_helper
# Create your models here.

class CollaborationRequest(model_helper.TimeBasedModel):
    collaborator = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.collaborator} is a collaborator on {self.project.name}'
