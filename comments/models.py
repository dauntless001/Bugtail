from django.db import models

from bugtail.helpers.model_helper import TimeBasedModel
from ckeditor.fields import RichTextField
# Create your models here.

class Comment(TimeBasedModel):
    issue = models.ForeignKey('projects.Issue', on_delete=models.CASCADE, related_name='issue')
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='comment_author')
    comment = RichTextField()


    def __str__(self):
        return f'{self.author} comment on issue {self.issue.slug} - {self.created_at.date()}'