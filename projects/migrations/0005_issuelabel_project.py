# Generated by Django 3.2.9 on 2021-11-10 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20211109_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuelabel',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projects.project'),
            preserve_default=False,
        ),
    ]
