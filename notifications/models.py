from django.db import models
from bugtail.helpers import model_helper
# Create your models here.
class Notification(model_helper.AuthorDescNameTimeBasedModel):
    name = None
    read = models.BooleanField(default=False)

    def __str__(self):
        return f'notification: {self.author} - {self.desc[:10]}'