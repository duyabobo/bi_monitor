# coding=utf-8
# author='duyabo'
# date='2017/11/13'

from django.conf.urls import url

from views import index

urlpatterns = [
    url(r'^$', index.index, name='index'),
    url(r'^list', index.email_list, name='list'),
    url(r'^content', index.email_detail, name='content'),
    url(r'^get_pager', index.get_pager, name='get_pager')
]
