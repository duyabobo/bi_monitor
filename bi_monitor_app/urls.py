# coding=utf-8
# author='duyabo'
# date='2017/11/13'

from django.conf.urls import url

from views import index

urlpatterns = [
    url(r'^$', index.index, name='index'),
    url(r'^content', index.content_detail, name='content'),
    url(r'^list', index.content_list, name='list'),
]
