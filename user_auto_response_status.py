#! -*-coding:utf-8 -*-
#!/usr/bin/python

# set_user_auto_response_stats(status) 在redis中设置用户自动回复的开启状态
# get_user_auto_response_stats(name) 查询该用户自动回复的开启状态

import redis
import json
import md5_name

hashname = 'user_auto_response_status'
r = redis.Redis(host="localhost", port="6379", db=0)

STATUS_NORMAL = 1  # 自动回复开启状态
STATUS_CLOSE = 2  # 自动回复关闭状态


def set_user_auto_response_stats(user_json):
    obj = None
    try:
        obj = json.loads(user_json)
    except:
        print '加载json出错：%s' % user_json
        return None
    md5_remark_name = md5_name.md5_name(obj['RemarkName'])
    try:
        r.hset(hashname, md5_remark_name, STATUS_NORMAL) if obj['status'] else r.hset(hashname, md5_remark_name, STATUS_CLOSE)
    except:
        print '插入redis失败:%s' % user_json


def get_user_auto_response_stats(RemarkName):
    md5_remark_name = md5_name.md5_name(RemarkName)
    res = r.hget(hashname, md5_remark_name)
    return res
