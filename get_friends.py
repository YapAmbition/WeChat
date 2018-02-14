#! -*-coding:utf-8 -*-
#!/usr/bin/python

# 获得我所有好友的信息
import itchat
import json
itchat.auto_login()  # 热登录，短时间内不必再登陆
friends = itchat.get_friends(update=True)[0:]
users = []
for friend in friends:
    users.append({'UserName':friend['UserName'],'Province':friend['Province'], 'City':friend['City'], 'NickName':friend['NickName'], 'RemarkName':friend['RemarkName'],'Sex':friend['Sex']})
print json.dumps(users)