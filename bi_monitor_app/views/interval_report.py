# coding=utf-8
# author='duyabo'
# date='2017/11/15'
from django.shortcuts import render


def index(request):
    return render(request, 'interval_report.html')
