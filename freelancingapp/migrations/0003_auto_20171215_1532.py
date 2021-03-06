# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-15 10:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('freelancingapp', '0002_freelancer_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='freelancer',
            name='is_freelancer',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='freelancer',
            name='is_recruiter',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='freelancer',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='recruiter',
            name='is_freelancer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='recruiter',
            name='is_recruiter',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='recruiter',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
