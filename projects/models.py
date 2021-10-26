from accounts.models import User
from django.db import models
from bugtail.helpers import model_helper
# Create your models here.

class Project(model_helper.AuthorDescNameTimeBasedModel):
    slug = models.SlugField(default=model_helper.gen_slug)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} {self.slug} project'
    

class Issue(model_helper.NameDescTimeBasedModel):
    # class IssueChoices(models.TextChoices):
    #     low = 'Low', 'Low'
    #     high = 'High', 'High'
    #     moderate = 'Moderate', 'Moderate'
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    slug = models.SlugField(default=model_helper.gen_slug)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Issue'
        verbose_name_plural = 'Issues'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.project.slug} task {self.slug} - {self.created_at.date()}' 

    

    