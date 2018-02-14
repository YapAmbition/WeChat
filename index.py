#!/usr/bin/python
# ! -*-coding:utf-8 -*-
# 执行函数，启动微信图灵机器人
import robot
import itchat
import user_msg_suf
import json
import sys
reload(sys)
sys.setdefaultencoding("utf8")

robot = robot.TuLing()


@itchat.msg_register([itchat.content.TEXT, itchat.content.PICTURE])
def TuLing_Reply(msg):  # 注册图灵机器人
    if msg['FromUserName'] == msg['ToUserName']:  # 给自己发消息
        do_some_cmd(msg)
    default_response = 'my net is wrong, so you is a shagou'
    response = ''
    if msg['Type'] == itchat.content.TEXT:
        response = robot.say(msg['Text'])
    if msg['Type'] == itchat.content.PICTURE:
        response = '别老发图了，我看不懂...'
    response = add_suf(msg['User']['RemarkName'] or msg['User']['NickName'], response)
    handle_msg(msg, response)
    return response or default_response


# 处理返回消息,记入文本中
def handle_msg(msg, response):
    username = msg['User']['RemarkName']
    if len(username) : username = msg['User']['NickName']
    message = msg['Text']
    ss = str(username) + ' : ' + str(message) + '\n' + 'I say : ' + str(response) + '\n'
    wechat_log = open('wechat.log', 'a')  # 写入文件
    wechat_log.write(ss)
    wechat_log.close()


# 添加后缀
def add_suf(RemarkName, text):
    suf = user_msg_suf.get_user_suf(RemarkName)
    if suf is not None and len(suf) > 0:
        text = '%s       ---%s' % (text, suf)
    return text

# 命令模式
def do_some_cmd(msg):
    text = msg['Text']
    if len(text) > 0 and text[0] == '$':  # 命令模式
        cmd = text[1:]
        params = cmd.split('&&')
        if params[0].upper() == 'USER_MSG_SUF':  # 添加后缀
            try:
                user_json = json.dumps({'RemarkName': params[1], 'suf': params[2]})
                user_msg_suf.set_user_suf(user_json)
                print '添加[%s]后缀[%s]成功' % (params[1], params[2])
            except:
                print '添加redis时出错：do_some_cmd,%s' % (json.dumps(msg))


# itchat.auto_login(hotReload=True, enableCmdQR=True)  # 用命令行二维码热登陆，在linux上登陆
# itchat.auto_login(hotReload=True)  # 热登录，短时间内不必再登陆
# itchat.login()  # 正常登陆，用二维码图片，在windows上登陆
# itchat.run()  # 启动注册的消息返回

# linux用下面登陆
# itchat.auto_login(hotReload=True, enableCmdQR=2)
itchat.auto_login(enableCmdQR=True)
itchat.run()
