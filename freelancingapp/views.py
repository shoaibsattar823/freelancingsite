# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from forms import RecruiterForm, FreelancerForm
from .models import Freelancer, Company, Recruiter


class HomePage(View):
    template_name = 'freelancingapp/home.html'
    def get(self, request):
        freelancers = Freelancer.objects.all()
        companies = Company.objects.all()
        return render(request, self.template_name,
                      {'freelancers': freelancers, 'companies': companies})


class HireTalent(View):
    template_name = 'freelancingapp/hire.html'

    def get(self, request):
        form = RecruiterForm()
        return render(request, self.template_name, {'form': form})


class TalentsView(View):
    template_name = 'freelancingapp/freelancer_list.html'

    def get(self, request):
        form = RecruiterForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RecruiterForm(request.POST)
        if form.is_valid():
            requirement = form.cleaned_data['to_hire']
            talents = Freelancer.objects.filter(expertise=requirement)
            return render(request, self.template_name, {'talents': talents})


class TalentDetailView(View):
    template_name = 'freelancingapp/freelancerdetails.html'

    def get(self, request):
        print "here: ", request.data


class FreelancerView(View):
    template_name = 'freelancingapp/freelance.html'

    def get(self, request):
        form = FreelancerForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = FreelancerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            expertise = form.cleaned_data['expertise']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            desc = form.cleaned_data['description']
            Freelancer.objects.get_or_create(name=name, expertise=expertise, email=email,
                                      username=username, description=desc)
            return HttpResponse('Thank You for joining our Freelancing Website!')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
