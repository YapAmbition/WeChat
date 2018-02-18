#! -*-coding:utf-8 -*-
#!/usr/bin/python

# 添加一些后缀到redis
import redis
import user_msg_suf
import json
import Szc_Log
import sys
reload(sys)
sys.setdefaultencoding("utf8")


hashname = 'user_msg_suf'
r = redis.Redis(host="localhost", port="6379", db=0)

add_dict = {
    '周芳芳':'致芳芳女神',  # 周芳芳
    '杨雪涛':'涛哥你就是个傻狗',  # 杨雪涛
    '罗媛':'罗媛我求求你别吃了~',  # 罗媛
    '崔源':'勇儿你嘛zeng噶~',  # 勇哥
    '蒋仕林':'40你困了',  # 蒋仕林
    '刘俊波':'社会我波哥？',  # 刘俊波
    '匡洋洋':'经理好 :)',  # 匡洋洋
    '陈榕':'女程序媛傻狗榕',  # 陈榕
    '李璐洁':'蛤？',  # 李璐洁
    '刘雨':'你是一条傻狗',  # 刘雨
}

for RemarkName, suf in add_dict.items():
    try:
        user_json = json.dumps({'RemarkName':RemarkName, 'suf':suf})
        user_msg_suf.set_user_suf(user_json)
        Szc_Log.debug('%s: 成功添加后缀:%s' % (__file__, user_json))
    except:
        Szc_Log.warning('%s: 添加redis时出错：%s,%s' % (__file__, RemarkName,suf))

print 'done'
