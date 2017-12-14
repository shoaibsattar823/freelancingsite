# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


CHOICES = (('Developer', 'Developer'),
           ('Designer', 'Designer'),
           ('Finance Expert', 'Finance Expert'))


class Freelancer(models.Model):
    name = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100, choices=CHOICES)
    email = models.EmailField(max_length=70, unique=True)
    username = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Recruiter(models.Model):
    to_hire = models.CharField(max_length=100, choices=CHOICES)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=70, unique=True)
    company = models.CharField(max_length=100)

    def __str__(self):
        return u'%s_%s' % (self.name, self.company)


class Company(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    website = models.URLField(max_length=200)

    class Meta:
        verbose_name_plural = 'companies'

    def __str__(self):
        return u'%s' % self.name
