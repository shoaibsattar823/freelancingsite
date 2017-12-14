from django.forms import ModelForm
from .models import *


class RecruiterForm(ModelForm):
    class Meta:
        model = Recruiter
        fields = '__all__'

class FreelancerForm(ModelForm):
    class Meta:
        model = Freelancer
        fields = '__all__'
