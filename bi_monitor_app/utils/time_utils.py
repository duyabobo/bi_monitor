# coding=utf-8
# author='duyabo'
# date='2017/11/22'
import time


def timestamp_to_string(stamp):
    """时间戳转字符串"""
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stamp/1000))
