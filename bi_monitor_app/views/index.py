# coding=utf-8
# author='duyabo'
# date='2017/11/15'
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def content_detail(request):
    """
    根据request中的api_id实现各种业务逻辑，查询各种类型的监控数据图表详情
    :param request:
    :return:
    """
    return render(
        request,
        'report_detail_2_dime.html',
        context={
            'table_dates': [
                [
                    'test_title_of_table',
                    [
                        ['时间', '接口名', '统计数目'],
                        ['2017-11-01 11:01:20', '/api/dashboard?', '20233']
                    ]
                ]
            ]
        }
    )


def content_list(request):
    """
    查询各种类型的监控数据列表
    :param request:
    :return:
    """
    return render(
        request,
        'report_list.html',
        context={
            'api_id': 'week_report_api_id',
            'title': 'test_title',
            'datas': [
                [1, '2017-11-01'],
                [2, '2017-11-08'],
                [3, '2017-11-15']
            ]
        }
    )
