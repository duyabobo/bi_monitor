# coding=utf-8
# author='duyabo'
# date='2017/11/13'

from django.conf.urls import url

from views import index

urlpatterns = [
    url(r'^$', index.index, name='index'),
]
