# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


CHOICES = (('Developer', 'Developer'),
           ('Designer', 'Designer'),
           ('Finance Expert', 'Finance Expert'))


class Freelancer(models.Model):
    name = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100, choices=CHOICES)
    email = models.EmailField(max_length=70, unique=True)
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Recruiter(models.Model):
    to_hire = models.CharField(max_length=100, choices=CHOICES)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=70, unique=True)
    work_type = models.CharField(max_length=100)
    company = models.CharField(max_length=100)

    def __str__(self):
        return u'%s_%s' % (self.name, self.company)