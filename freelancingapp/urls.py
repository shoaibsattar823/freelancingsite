from django.conf.urls import url
from django.contrib.auth import views as auth_views
from freelancingapp import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view()),
    url(r'^login/$', auth_views.login),
    url(r'^logout/$', views.logout_view),
    url(r'^hire/$', views.HireTalent.as_view()),
    url(r'^freelance/$', views.FreelancerView.as_view()),
    url(r'^talents/$', views.TalentsView.as_view()),
    url(r'^talents/([\w ]+)$', views.TalentDetailView.as_view()),
]
