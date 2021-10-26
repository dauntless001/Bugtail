from django.db import models
from django.utils.crypto import get_random_string
from accounts.models import User


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
    desc = models.TextField()

    class Meta:
        abstract = True


class AuthorNameTimeBasedModel(NameTimeBasedModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class AuthorDescNameTimeBasedModel(AuthorNameTimeBasedModel):
    desc = models.TextField()

    class Meta:
        abstract = True

