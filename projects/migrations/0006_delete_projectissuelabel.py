# Generated by Django 3.2.9 on 2021-11-10 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_issuelabel_project'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProjectIssueLabel',
        ),
    ]