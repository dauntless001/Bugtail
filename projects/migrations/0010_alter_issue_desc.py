# Generated by Django 3.2.9 on 2021-12-08 11:25

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_issue_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='desc',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
