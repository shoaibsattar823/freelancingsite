from django.forms import ModelForm
from django import forms
from .models import *


class RecruiterForm(ModelForm):
    class Meta:
        model = Recruiter
        exclude = ['user', 'username', 'is_recruiter', 'is_freelancer']


class FreelancerForm(ModelForm):
    class Meta:
        model = Freelancer
        exclude = ['user', 'username', 'is_recruiter', 'is_freelancer']


class HireForm(forms.Form):
    expertise = forms.ChoiceField(choices=CHOICES)


class JobPostForm(ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
