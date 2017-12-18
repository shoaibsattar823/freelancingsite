# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Recruiter, Freelancer, Company, Job

admin.site.register(Freelancer)
admin.site.register(Recruiter)
admin.site.register(Company)
admin.site.register(Job)
