# coding=utf-8
# author='duyabo'
# date='2017/11/22'
import random
import time
from bi_monitor_app.models import *


def f1():
    """创建时报记录"""
    for i in range(500):
        now = time.time()*1000
        delta1 = random.randint(1, 1000) * 1000
        HourAnalysis(from_timestamp=now - delta1,
                     end_timestamp=now - delta1 - 3600000).save()


def f2():
    """创建时报统计信息数据"""
    for i in range(500):
        for source in [0, 1]:
            for kind in range(8):
                BiAccessAnalysis(
                    hour_analysis_id=i,
                    source=source,
                    kind=kind,
                    num=random.randint(1, 1000),
                    percent=random.randint(1, 100),
                    average=random.randint(1, 1000)
                ).save()


def f3():
    """创建值得关注的访问记录信息"""
    for i in range(500):
        timestramp = time.time() - random.randint(1, 1000)*1000
        for source in [0, 1]:
            for num in range(random.randint(1, 8)):
                NoteWorthyLog(
                    hour_analysis_id=i,
                    source=source,
                    access_timestamp=timestramp,
                    report_name='report_name',
                    report_id='report_id',
                    user_name='user_name',
                    delay_microseconds=random.random()*1000,
                    parameters='parameters',
                    department_name='department_name',
                    api_key='api_key'
                ).save()
