# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from forms import RecruiterForm, FreelancerForm, HireForm, JobPostForm
from .models import Freelancer, Company, Recruiter, Job


class HomePage(View):
    template_name = 'freelancingapp/home.html'
    freelancers = Freelancer.objects.all()
    companies = Company.objects.all()

    def get(self, request):
        if Freelancer.objects.filter(username=request.user).exists():
            usertype = 'freelancer'
        else:
            usertype = 'recruiter'

        context = {'freelancers': self.freelancers,
                   'companies': self.companies,
                   'usertype': usertype}

        return render(request, self.template_name, context)


class RecruiterSignUp(TemplateView):
    template_name = 'freelancingapp/recruitersignup.html'

    def get_context_data(self, **kwargs):
        context = super(RecruiterSignUp, self).get_context_data(**kwargs)
        context['recruiter_form'] = RecruiterForm()
        context['user_form'] = UserCreationForm()
        return context


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
            username = user_form.cleaned_data['username']
            recruiter = recruiter_form.save(commit=False)
            recruiter.user = user
            recruiter.username = username
            recruiter.save()
            login(request, user)
            return HttpResponseRedirect('/')
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
            username = user_form.cleaned_data['username']
            freelancer = freelancer_form.save(commit=False)
            freelancer.user = user
            freelancer.username = username
            freelancer.save()
            login(request, user)
            return HttpResponseRedirect('/freelance/')


class FreelancerView(View):
    template_name = 'freelancingapp/freelance.html'

    def get(self, request):
        freelancer = Freelancer.objects.get(username=request.user)
        jobs = Job.objects.filter(required_skills=freelancer.expertise)
        jobs = [job.designation for job in jobs]
        return render(request, self.template_name, {'jobs': jobs})


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


class PostJob(View):
    template_name = 'freelancingapp/post-job.html'

    def get(self, request):
        form = JobPostForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = JobPostForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            return render(request, self.template_name, {'data': data})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
