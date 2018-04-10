#!/usr/bin/python
# ! -*-coding:utf-8 -*-

"""
微信机器人控制器类
在类中添加成员变量作为控制功能的开关
"""

import WechatResponse


class WechatRobotController:

    def __init__(self):
        """
        构造函数
        robot: 自动回复机器人
        GLOBAL_AUTO_RESPONSE: 全局自动回复开关
        CSU_RJXY_NOTIFY: {status:, chatroomName:} 软件学院通知读取
        """
        self.wechat_response = WechatResponse.WechatResponse()
        self.global_auto_response = False  # 是否开启自动回复
        self.csu_rjxy_notify = False  # 是否打开软件学院通知
