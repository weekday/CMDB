#coding:utf-8

from django.conf.urls import url
from views import host

urlpatterns = [
    url(r'^host.html$',host,name='host'),
]