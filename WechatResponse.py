#!/usr/bin/python
# ! -*-coding:utf-8 -*-
"""
微信自动回复内容
默认会调用图灵机器人api
特殊情况可以自己控制返回
"""
import robot
import itchat


class WechatResponse:

    def __init__(self):
        """
        通过图灵机器人进行回复
        初始化图灵机器人
        """
        self.tulingRobot = robot.TuLing()

    def get_response(self, msg):
        """
        目前只对文本内容进行返回
        :param msg:
        :return:
        """
        if msg['Type'] == itchat.content.TEXT:
            return self.tulingRobot.say(msg['Text'])
