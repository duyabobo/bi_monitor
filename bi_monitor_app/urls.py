# coding=utf-8
# author='duyabo'
# date='2017/11/13'

from django.conf.urls import url

from views import index, detail, search

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^(?P<report_id>[0-9]+)/$', detail, name='detail'),
    url(r'^search/$', search, name='search'),
]
