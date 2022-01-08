from accounts.models import Profile, User
from django.db.models.signals import post_save

def account_post_save(sender, instance, created, *args, **kwargs):
    if created:
        email = instance.email
        user = User.objects.get(email=email)
        Profile.objects.create(user=user)


post_save.connect(account_post_save, sender=User)
 

'''
Import signal
from django.db.models.signals import post_save
create signal method def blog_post_save(sender, instance, *args, **kwargs)
connect to signal  eg. post_save.connect(signal_method, sender=)
'''