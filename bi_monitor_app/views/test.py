# coding=utf-8
# author='duyabo'
# date='2017/11/15'
from django.shortcuts import render


def test(request):
    return render(request, 'base.html')
