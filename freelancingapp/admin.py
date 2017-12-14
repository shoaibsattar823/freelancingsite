# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Recruiter, Freelancer, Company

admin.site.register(Freelancer)
admin.site.register(Recruiter)
admin.site.register(Company)
