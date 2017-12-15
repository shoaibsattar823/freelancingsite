# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from forms import RecruiterForm, FreelancerForm, HireForm
from .models import Freelancer, Company, Recruiter


class HomePage(View):
    template_name = 'freelancingapp/home.html'

    freelancers = Freelancer.objects.all()
    companies = Company.objects.all()
    def get(self, request):
        if (Freelancer.objects.filter(username=request.user)).exists():
            usertype = 'freelancer'
            return render(request, self.template_name,
                          {'freelancers': self.freelancers,
                           'companies': self.companies,
                           'usertype': usertype
                           })
        else:
            usertype = 'recruiter'
            return render(request, self.template_name,
                          {'freelancers': self.freelancers,
                           'companies': self.companies,
                           'usertype': usertype
                           })


class RecruiterSignUp(View):
    template_name = 'freelancingapp/recruitersignup.html'

    def get(self, request):
        recruiter_form = RecruiterForm()
        user_form = UserCreationForm()
        return render(request, self.template_name,
                      {'recruiter_form': recruiter_form,
                       'user_form': user_form})


class RecruiterHome(View):

    def get(self, request):
        recruiter_form = RecruiterForm()
        user_form = UserCreationForm()
        return HttpResponseRedirect('/')

    def post(self, request):
        recruiter_form = RecruiterForm(request.POST)
        user_form = UserCreationForm(request.POST)
        if recruiter_form.is_valid() and user_form.is_valid():
            user = user_form.save()
            rec_data = recruiter_form.cleaned_data
            name = rec_data['name']
            username = user_form.cleaned_data['username']
            email = rec_data['email']
            company = rec_data['company']
            to_hire = rec_data['to_hire']
            Recruiter.objects.create(user=user, name=name, username=username,
                                     email=email, company=company)
            raw_password = user_form.cleaned_data.get('password1')
            talents = Freelancer.objects.filter(expertise=expertise)
            login(request, user)
            return HttpResponseRedirect('/hire/')
        else:
            return HttpResponseRedirect('/recruitersignup/')


class FreelancerSignUp(View):
    template_name = 'freelancingapp/freelancesignup.html'

    def get(self, request):
        user_form = UserCreationForm()
        freelancer_form = FreelancerForm()
        return render(request, self.template_name,
                      {'user_form': user_form,
                       'freelancer_form': freelancer_form})

    def post(self, request):
        user_form = UserCreationForm(request.POST)
        freelancer_form = FreelancerForm(request.POST)
        if user_form.is_valid() and freelancer_form.is_valid():
            user = user_form.save()
            name = freelancer_form.cleaned_data['name']
            expertise = freelancer_form.cleaned_data['expertise']
            email = freelancer_form.cleaned_data['email']
            username = user_form.cleaned_data['username']
            desc = freelancer_form.cleaned_data['description']
            Freelancer.objects.create(user=user, name=name, expertise=expertise,
                                      email=email, username=username,
                                      description=desc)
            login(request, user)
            return HttpResponseRedirect('/freelance/')


class FreelancerView(View):
    template_name = 'freelancingapp/freelance.html'

    def get(self, request):
        return render(request, self.template_name)


class HireTalent(View):
    template_name = 'freelancingapp/hire.html'
    def get(self, request):
        form = HireForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = HireForm(request.POST)
        if form.is_valid():
            expertise = form.cleaned_data['expertise']
            talents = Freelancer.objects.filter(expertise=expertise)
            return render(request, self.template_name, {'talents': talents})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
