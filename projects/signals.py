from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from projects.models import IssueLabel, Project


@receiver(post_save, sender=Project)
def save_projects(sender, instance,created, **kwargs):
    if created:
        labels = instance.issuelabel_set.all()
        if labels.count() <= 0:
            label = IssueLabel.objects.bulk_create([
                IssueLabel(project=instance, name='Open', short_name='open', color='#16537e'),
                IssueLabel(project=instance, name='selected for development', short_name='sfd', color='#1889de'),
                IssueLabel(project=instance, name='in progress', short_name='inp', color='#6699CC'),
                IssueLabel(project=instance, name='code review', short_name='cdrw', color='#1B4737'),
                IssueLabel(project=instance, name='completed', short_name='cpd', color='#CD5B45'),
            ])
