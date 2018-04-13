#!/usr/bin/python
# ! -*-coding:utf-8 -*-

# 日志按日打印
# 日志模块 日志级别：debug < warning < fatal
# debug: 调试时打印的信息
# warning: 程序报错打印的信息，但不会使整个程序崩溃
# fatal: 程序出错打印的信息，会使应用程序直接崩溃

import time

LOG_DIR = './log/'  # 日志存放目录
PROJECT_NAME = 'wechat'  # 项目名，日志前缀


# 根据当前时间得到日志名
def get_log_name(log_level_str):
    timestr = time.strftime("%Y%m%d", time.localtime(time.time()))
    logname = "%s.%s_%s.log" % (PROJECT_NAME, timestr, log_level_str)
    log_dir = (LOG_DIR + '/') if LOG_DIR[-1] != '/' else LOG_DIR
    full_log_name = log_dir + logname
    return full_log_name


def debug(ss):
    """
    打印debug日志
    :param ss:
    :return:
    """
    if ss is not None:
        log_name = get_log_name('debug')
        logfile = None
        try:
            logfile = open(log_name, 'a')
            logfile.write(ss)
            logfile.write("\n")
        except IOError, e:
            print "input debug log error: [%s]" % str(e)
        finally:
            if logfile is not None: logfile.close()


def warning(ss):
    """
    打印warning日志
    :param ss:
    :return:
    """
    if ss is not None:
        log_name = get_log_name('warning')
        logfile = None
        try:
            logfile = open(log_name, 'a')
            logfile.write(ss)
            logfile.write("\n")
        except IOError, e:
            print "input debug log error: [%s]" % str(e)
        finally:
            if logfile is not None: logfile.close()


def fatal(ss):
    """
    打印fatal日志
    :param ss:
    :return:
    """
    if ss is not None:
        log_name = get_log_name('fatal')
        logfile = None
        try:
            logfile = open(log_name, 'a')
            logfile.write(ss)
            logfile.write("\n")
        except IOError, e:
            print "input debug log error: [%s]" % str(e)
        finally:
            if logfile is not None: logfile.close()


