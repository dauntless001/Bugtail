# Generated by Django 3.2.9 on 2021-12-08 08:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_remove_issue_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='desc',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
