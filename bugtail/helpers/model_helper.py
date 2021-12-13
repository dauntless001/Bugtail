from django.db import models
from django.db.models.fields import TextField
from django.utils.crypto import get_random_string
from accounts.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

def gen_slug():
    return get_random_string(length=8)

class TimeBasedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class NameTimeBasedModel(TimeBasedModel):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True

class NameDescTimeBasedModel(NameTimeBasedModel):
    desc = TextField()

    class Meta:
        abstract = True


class AuthorNameTimeBasedModel(NameTimeBasedModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class AuthorDescNameTimeBasedModel(NameDescTimeBasedModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

