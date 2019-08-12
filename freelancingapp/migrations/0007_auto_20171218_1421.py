# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-18 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelancingapp', '0006_job'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='company',
        ),
        migrations.AddField(
            model_name='job',
            name='required_skills',
            field=models.CharField(choices=[('Developer', 'Developer'), ('Designer', 'Designer'), ('Finance Expert', 'Finance Expert')], max_length=100, null=True),
        ),
    ]
