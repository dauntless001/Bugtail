from django.db import models
from bugtail.helpers import model_helper
# Create your models here.

class Project(model_helper.AuthorDescNameTimeBasedModel):
    slug = models.SlugField(default=model_helper.gen_slug)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} {self.slug} project'
    