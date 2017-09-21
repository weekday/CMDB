"""CMDB URL Configuration

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
from index.views import index,login_view,logout,error
from django.conf.urls import handler404,handler500
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$',index),
	url(r'^index/',index),
	url(r'^index.html$',index),
	url(r'^login.html$',login_view),
	url(r'^login/',login_view),
	url(r'^logout.html',logout),
	url(r'^error.html$',error),
	url(r'^host/', include('hostinfo.urls')),
]
