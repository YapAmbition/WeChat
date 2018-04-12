#!/usr/bin/python
# ! -*-coding:utf-8 -*-

"""
重构微信自动回复机器人
将机器人的核心功能(自动回复机器人)封装在本文件中
"""

import itchat
import WechatRobotController
import WechatRobotCommand
import thread
import sys
reload(sys)
sys.setdefaultencoding("utf8")

"""
init start
初始化整个工程
创建wechat_robot_controller控制对象(所有的线程应该由某一变量动态控制)
需要开发新的功能时,若需要开启新的线程,应该在WechatRobotController.py中添加成员变量作为线程的开关
"""
wechat_robot_controller = WechatRobotController.WechatRobotController()
wechat_robot_command = WechatRobotCommand.WechatRobotCommand(wechat_robot_controller)
"""
init finish
"""


def say_to_nikfce(msg=None):
    """
    对自己的群里说
    :param msg:
    :return:
    """
    chatroom = itchat.search_chatrooms(name=u'nikfce')
    if msg is not None: itchat.send_msg(msg, toUserName=chatroom[0]['UserName'])


def say_to_1406(msg=None):
    """
    对班群说
    :param msg: 说的内容
    :return:
    """
    chatroom = itchat.search_chatrooms(name=u'软件1406班群')
    if msg is not None: itchat.send_msg(msg, toUserName=chatroom[0]['UserName'])


@itchat.msg_register([itchat.content.TEXT])
def auto_response_robot(msg):
    """
    实现微信机器人两个功能:1.命令模式(通过新建线程的形式完成消息反馈) 2.图灵机器人自动回复
    :param msg:注册消息拦截
    :return:返回回复的消息
    """
    text = msg['Text']
    from_user_name = msg['FromUserName']  # 发送者
    if from_user_name == msg['ToUserName']:  # 如果是给自己发消息，判断是否是命令模式
        if len(text) > 0 and text[0] == '$':
            command = text[1:]
            cmd_response = wechat_robot_command.handle_command(command)
            thread.start_new_thread(say_to_nikfce, (cmd_response,))
    else:
        return wechat_robot_controller.wechat_response.get_response(msg) if wechat_robot_controller.global_auto_response else None


def login_with_picture():
    """
    用于在有图形界面的机器上暂时登陆
    :return:
    """
    itchat.login()  # 正常登陆，用二维码图片，在windows上登陆
    itchat.run()


def hot_login_with_picture():
    """
    用于在有图形界面的机器上热登陆,多用于测试
    :return:
    """
    itchat.auto_login(hotReload=True)  # 正常登陆，用二维码图片，短时间内无需再次扫码
    itchat.run()  # 启动注册的消息返回


def login_with_cmd_qr(enable_cmd_qr=True):
    """
    用于命令行暂时登陆
    :param enable_cmd_qr: 可以通过填非0的整型数来控制命令行二维码缩放比例,负数表示反色显示
    :return:
    """
    itchat.login(enableCmdQR=enable_cmd_qr)
    itchat.run()


def hot_login_with_cmd_qr(enable_cmd_qr=True):
    """
    用于命令行热登陆,多用于测试
    :param enable_cmd_qr: 可以通过填非0的整型数来控制命令行二维码缩放比例,负数表示反色显示
    :return:
    """
    itchat.auto_login(hotReload=True, enableCmdQR=enable_cmd_qr)
    itchat.run()
