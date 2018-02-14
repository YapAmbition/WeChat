#!/usr/bin/python
# ! -*-coding:utf-8 -*-

import requests


class TuLing:
    def __init__(self):
        self.apiUrl = 'http://www.tuling123.com/openapi/api'
        self.key = '4bf3ec145c354cab821b4afeb33ecacb'
        self.user_id = '一只傻狗'

    def say(self, msg):
        data = {
            'key': self.key,
            'info': msg,
            'userid': self.user_id,  # 这里你想改什么都可以
        }
        response = requests.post(self.apiUrl, data=data).json()
        response_msg = response['text']
        return response_msg

