#! -*-coding:utf-8 -*-
#!/usr/bin/python

# set_user_suf:输入json信息{"userid":"12345","suf":"蛤？"},将其保存在redis中
# get_user_suf:当id为userid的人跟你聊天时，在回复时会直接回复suf中内容

import redis
import json
import md5_name

hashname = 'user_msg_suf'
r = redis.Redis(host="localhost", port="6379", db=0)
user_suf = {}

# 将用户信息存入内存和redis
def set_user_suf(user_json):
    obj = None
    try:
        obj = json.loads(user_json)
        print '在redis中插入了数据%s' % user_json
    except:
        print '加载json出错：%s' % user_json
        return None
    md5_remark_name = md5_name.md5_name(obj['RemarkName'])
    user_suf[md5_remark_name] = obj['suf']
    try:
        r.hset(hashname, md5_remark_name, obj['suf'])
    except:
        print '插入redis失败:%s' % user_json

# 获得该用户的内容后缀
def get_user_suf(RemarkName):
    md5_remark_name = md5_name.md5_name(RemarkName)
    res = None if not user_suf.has_key(md5_remark_name) else user_suf[md5_remark_name]
    if res is None :
        res = r.hget(hashname, md5_remark_name)
        if res is not None:
            user_suf[md5_remark_name] = res
    return res
