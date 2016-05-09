"""myproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'tuanapp.views.index'),
    url(r'^index$', 'tuanapp.views.index'),
    url(r'^index/$', 'tuanapp.views.index'),
    url(r'^create_tuan$', 'tuanapp.views.create_tuan'),
    url(r'^create_tuan/$', 'tuanapp.views.create_tuan'),
    url(r'insert$', 'tuanapp.views.insert'),
    url(r'vote$', 'tuanapp.views.vote'),
    url(r'update$', 'tuanapp.views.update'),
    url(r'delete$', 'tuanapp.views.delete'),  
	url(r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name': 'login.html'}),
	url(r'^login/$', 'tuanapp.views.Login'),
	url(r'^acc_login/$','tuanapp.views.acc_login'),
	url(r'^logout/$', 'tuanapp.views.logout_view'),
	url(r'^register/$','tuanapp.views.register'),
	url(r'^register_create/$','tuanapp.views.register_create'),
    url(r'^my_tuan', 'tuanapp.views.my_tuan'),  
]
