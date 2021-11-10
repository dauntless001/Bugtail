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
    


class IssueLabel(model_helper.TimeBasedModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=10)
    short_name = models.CharField(max_length=5)

    class Meta:
        verbose_name = 'Issue Label'
        verbose_name_plural = 'Issue Labels'

    def __str__(self):
        return f'{self.project.name} - {self.name}'





class Issue(model_helper.NameDescTimeBasedModel):
    class IssuePriorityChoices(models.TextChoices):
        low = 'Low', 'Low'
        high = 'High', 'High'
        moderate = 'Moderate', 'Moderate'
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    slug = models.SlugField(default=model_helper.gen_slug)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, 
        blank=True, related_name='issue_assignee')
    priority = models.CharField(max_length=100, choices=IssuePriorityChoices.choices,
    default=IssuePriorityChoices.moderate)
    label = models.ForeignKey(IssueLabel, on_delete=models.SET_NULL, null=True, blank=True,
    related_name='issue_label')


    class Meta:
        verbose_name = 'Issue'
        verbose_name_plural = 'Issues'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.project.slug} task {self.slug} - {self.created_at.date()}' 

    def assginee_image(self):
        return self.assigned_to.profile.image_url()

    