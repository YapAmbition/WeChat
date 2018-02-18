#! -*-coding:utf-8 -*-
#!/usr/bin/python

# set_user_auto_response_status(status) 在redis中设置用户自动回复的开启状态
# get_user_auto_response_status(name) 查询该用户自动回复的开启状态

import redis
import json
import md5_name
import Szc_Log

hashname = 'user_auto_response_status'
r = redis.Redis(host="localhost", port="6379", db=0)

STATUS_NORMAL = 1  # 自动回复开启状态
STATUS_CLOSE = 2  # 自动回复关闭状态


def set_user_auto_response_status(user_json):
    try:
        obj = json.loads(user_json)
        md5_remark_name = md5_name.md5_name(obj['RemarkName'])
        r.hset(hashname, md5_remark_name, obj['status'])
        Szc_Log.debug('%s: 修改%s的user_auto_response_status为%s' % (__file__, obj['RemarkName'], obj['status']))
    except:
        Szc_Log.warning('%s: 修改用户user_auto_response_status出错：%s' % (__file__, user_json))


def get_user_auto_response_status(RemarkName):
    return r.hget(hashname, md5_name.md5_name(RemarkName))
