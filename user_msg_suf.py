#! -*-coding:utf-8 -*-
#!/usr/bin/python

# set_user_suf:输入json信息{"userid":"12345","suf":"蛤？"},将其保存在redis中
# get_user_suf:当id为userid的人跟你聊天时，在回复时会直接回复suf中内容

import redis
import json
import md5_name
import Szc_Log

hashname = 'user_msg_suf'
r = redis.Redis(host="localhost", port="6379", db=0)


# 将用户信息存入内存和redis
def set_user_suf(user_json):
    try:
        obj = json.loads(user_json)
        md5_remark_name = md5_name.md5_name(obj['RemarkName'])
        r.hset(hashname, md5_remark_name, obj['suf'])
        Szc_Log.debug('%s: 在redis中插入了数据%s' % (__file__, user_json))
    except:
        Szc_Log.warning('%s: 加载json出错：%s' % (__file__, user_json))


# 获得该用户的内容后缀
def get_user_suf(RemarkName):
    return r.hget(hashname, md5_name.md5_name(RemarkName))
