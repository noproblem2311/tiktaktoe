# Generated by Django 4.0.5 on 2022-07-02 16:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_profile_bookmarklist_counterpost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='counterpost',
            name='created_by',
        ),
        migrations.AddField(
            model_name='counterpost',
            name='created_by',
            field=models.ManyToManyField(default=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
