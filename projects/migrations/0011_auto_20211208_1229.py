# Generated by Django 3.2.9 on 2021-12-08 11:29

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_alter_issue_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='author',
        ),
        migrations.AlterField(
            model_name='issue',
            name='desc',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='desc',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]