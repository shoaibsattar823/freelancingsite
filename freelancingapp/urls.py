from django.conf.urls import url
from django.contrib.auth import views as auth_views
from freelancingapp import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view()),
    url(r'^login/$', auth_views.login),
    url(r'^logout/$', views.logout_view),
    url(r'^recruitersignup/$', views.RecruiterSignUp.as_view()),
    url(r'^freelancesignup/$', views.FreelancerSignUp.as_view()),
    url(r'^recruiter/$', views.RecruiterHome.as_view()),
    url(r'^hire/$', views.HireTalent.as_view()),
    url(r'^freelance/$', views.FreelancerView.as_view()),
    url(r'^job-posting/$', views.PostJob.as_view()),
]
