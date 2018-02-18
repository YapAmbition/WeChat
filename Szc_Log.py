#!/usr/bin/python
# ! -*-coding:utf-8 -*-

# 日志按日打印
# 日志模块 日志级别：debug < warning < fatal
# debug: 调试时打印的信息
# warning: 程序报错打印的信息，但不会使整个程序崩溃
# fatal: 程序出错打印的信息，会使应用程序直接崩溃

import time

LOG_DIR = '/Users/shenzhencheng/Documents/pycharm/WeChat'  # 日志存放目录
PROJECT_NAME = 'wechat'  # 项目名，日志前缀

# 定义错误级别常量
DEBUG = 1
WARNING = 2
FATAL = 3
LOG_LEVEL = {1: 'debug', 2: 'warning', 3: 'fatal'}


# 根据当前时间得到日志名
def get_log_name(log_level_str):
    global LOG_DIR
    timestr = time.strftime("%Y%m%d", time.localtime(time.time()))
    logname = "%s.%s_%s.log" % (PROJECT_NAME, timestr, log_level_str)
    LOG_DIR = (LOG_DIR + '/') if LOG_DIR[-1] != '/' else LOG_DIR
    full_log_name = LOG_DIR + logname
    return full_log_name


def debug(ss):
    log_name = get_log_name(LOG_LEVEL[DEBUG])
    logfile = open(log_name, 'a')
    logfile.write(ss)
    logfile.write("\n")
    logfile.close()


def warning(ss):
    log_name = get_log_name(LOG_LEVEL[WARNING])
    logfile = open(log_name, 'a')
    logfile.write(ss)
    logfile.write("\n")
    logfile.close()


def fatal(ss):
    log_name = get_log_name(LOG_LEVEL[FATAL])
    logfile = open(log_name, 'a')
    logfile.write(ss)
    logfile.write("\n")
    logfile.close()

