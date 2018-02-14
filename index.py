#!/usr/bin/python
# ! -*-coding:utf-8 -*-
# 执行函数，启动微信图灵机器人
import robot
import itchat
import user_msg_suf
import user_auto_response_status
import json
import time
import sys
reload(sys)
sys.setdefaultencoding("utf8")

# 初始化代码块
robot = robot.TuLing() # 初始化图灵机器人
GLOBAL_AUTO_RESPONSE = True # 是否开启自动回复


@itchat.msg_register([itchat.content.TEXT, itchat.content.PICTURE])
def TuLing_Reply(msg):  # 注册图灵机器人
    if msg['FromUserName'] == msg['ToUserName']: do_some_cmd(msg) # 如果是给自己发消息，判断是否是命令模式
    # //todo 很不好的做法
    # 如果全局自动回复开启，则正常返回自动回复,
    if GLOBAL_AUTO_RESPONSE : response = get_response(msg)
    else : return None
    handle_msg(msg, response) # 在日志中记录下聊天信息
    return response

# 返回正确的返回
def get_response(msg):
    if user_auto_response_status.STATUS_CLOSE == user_auto_response_status.get_user_auto_response_stats(msg['User']['RemarkName']) : return None  # 如果该用户的自动回复状态为false直接不返回
    response = ''
    if msg['Type'] == itchat.content.TEXT:
        response = robot.say(msg['Text'])
    if msg['Type'] == itchat.content.PICTURE:
        response = '本机器人看不懂图...'
    response = add_suf(msg['User']['RemarkName'] or msg['User']['NickName'], response) # 添加后缀功能
    return response


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
                print '添加[%s]后缀[%s]成功,time:%s' % (params[1], params[2], time.time())
            except:
                print '添加redis时出错：do_some_cmd,%s' % (json.dumps(msg))
        elif params[0].upper() == 'SET_AUTO_RESPONSE': # 设置全局自动回复
            global GLOBAL_AUTO_RESPONSE
            GLOBAL_AUTO_RESPONSE = True if params[1] else False
            print '设置全局自动回复，time:%s' % time.time()
        elif params[0].upper() == 'SET_USER_AUTO_RESPONSE': # 设置某人的自动回复
            user_json = json.dumps({'RemarkName': params[1], 'status': params[2]})
            user_auto_response_status.set_user_auto_response_stats(user_json)
            print '设置%s的自动回复状态为%s,time:%s' % (params[1], params[2], time.time())


# itchat.auto_login(hotReload=True, enableCmdQR=True)  # 用命令行二维码热登陆，在linux上登陆
# itchat.auto_login(hotReload=True)  # 热登录，短时间内不必再登陆
# itchat.login()  # 正常登陆，用二维码图片，在windows上登陆
# itchat.run()  # 启动注册的消息返回

# linux用下面登陆
# itchat.auto_login(hotReload=True, enableCmdQR=2)
itchat.auto_login(enableCmdQR=True)
itchat.run()
