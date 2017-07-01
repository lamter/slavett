# coding:utf-8
import json
import os


class Data(object):
    """
    服务器的数据
    """

    def __init__(self):
        futures_holiday_file = os.path.join(os.path.split(__file__)[0], 'futures_holiday.json')
        with open(futures_holiday_file, 'r') as f:
            self.futures_holiday = f.read()
