from django.db import models
from django.contrib.auth.models import AbstractUser
from bugtail.helpers import image_helper
from django.conf import settings
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='Something amazing about me')
    profile_pic = models.ImageField(upload_to=image_helper.get_upload_path, null=True, blank=True)
    # image here

    def __str__(self):
        return f'{self.user.email} Profile'
    
    def image_url(self):
        if self.profile_pic:
            return getattr(self.profile_pic, 'url', None)
        else:
            return f'{settings.STATIC_URL}img/avatars/avatar-2.jpg'