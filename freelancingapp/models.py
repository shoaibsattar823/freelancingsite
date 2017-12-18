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
    user = models.OneToOneField(User, default='', null=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=70, unique=True)
    expertise = models.CharField(max_length=100, choices=CHOICES)
    description = models.TextField(null=True, blank=True)
    is_freelancer = models.BooleanField(default=True)
    is_recruiter = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Recruiter(models.Model):
    user = models.OneToOneField(User, default='', null=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=70, unique=True)
    company = models.CharField(max_length=100)
    to_hire = models.CharField(max_length=100, choices=CHOICES, null=True, blank=True)
    is_freelancer = models.BooleanField(default=False)
    is_recruiter = models.BooleanField(default=True)

    def __str__(self):
        return u'%s_%s' % (self.name, self.company)


class Job(models.Model):
    designation = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    required_skills = models.CharField(max_length=100, choices=CHOICES, null=True)

    def __str__(self):
        return u'%s' % self.designation


class Company(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    website = models.URLField(max_length=200)

    class Meta:
        verbose_name_plural = 'companies'

    def __str__(self):
        return u'%s' % self.name
