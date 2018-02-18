#! -*-coding:utf-8 -*-
#!/usr/bin/python

# 用md5加密用户名


import hashlib


def md5_name(name):
    m = hashlib.md5()
    m.update(name)
    return m.hexdigest()