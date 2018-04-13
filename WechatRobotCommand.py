#!/usr/bin/python
# ! -*-coding:utf-8 -*-
"""
所有的命令在本文件中定义
命令名即方法名
如果需要在命令中向微信群发送消息,需要新建一个线程,因为itchat是阻塞式的
"""
import datetime
import ScanMysqlForNotify
import thread
import Szc_Log


class WechatRobotCommand:

    def __init__(self, wechat_robot_controller):
        """
        声明该类的成员变量
        """
        self.command = None
        self.wechatRobotController = wechat_robot_controller
        self.cmdList = []
        self.helpList = {
            "HELP": {"desc": "获得能使用的所有命令"},
            "SAY_HELLO": {"desc": "向nikfce发送{msg},测试用", "msg": "* 待发送的内容"},
            "SET_AUTO_RESPONSE_STATUS": {"desc": "设置自动回复状态为{status}(默认为False)", "status":"自动回复状态值,当状态为True时开启自动回复"},
            "GET_AUTO_RESPONSE_STATUS": {"desc": "获取当前自动回复状态值"},
            "START_CSU_RJXY_NOTIFY": {"desc": "开启自动发送院内通知"},
            "STOP_CSU_RJXY_NOTIFY": {"desc": "停止自动发送院内通知"},
            "GET_CSU_RJXY_NOTIFY_STATUS": {"desc": "获得当前自动发送院内通知状态"},
        }

    def handle_command(self, command):
        """
        执行注入的各种命令,命令名需和函数名一致(规范)
        对于没一个命令返回都需要在之前添加时间(datetime.datetime.now()),并在返回的内容中包含使用的命令
        :param command 需要执行的命令
        :return: 各命令返回的值,最终会被发送到nikfce群中
        """
        self.command = command
        self.cmdList = command.split('&&')
        if self.cmdList[0].upper() == "HELP": return self.help()
        elif self.cmdList[0].upper() == "SAY_HELLO": return self.say_hello()
        elif self.cmdList[0].upper() == "SET_AUTO_RESPONSE_STATUS": return self.set_auto_response_status()
        elif self.cmdList[0].upper() == "GET_AUTO_RESPONSE_STATUS": return self.get_auto_response_status()
        elif self.cmdList[0].upper() == "START_CSU_RJXY_NOTIFY": return self.start_csu_rjxy_notify()
        elif self.cmdList[0].upper() == "STOP_CSU_RJXY_NOTIFY": return self.stop_csu_rjxy_notify()
        elif self.cmdList[0].upper() == "GET_CSU_RJXY_NOTIFY_STATUS": return self.get_csu_rjxy_notify_status()

    def help(self):
        """
        获得能使用的所有命令
        :return:
        """
        result = ""
        for cmd_name, cmd_desc in self.helpList.iteritems():
            result += cmd_name
            result += "("
            for k, v in cmd_desc.iteritems():
                if k is not "desc":
                    result += k
                    result += ": "
                    result += v
                    result += "; "
            result += "): "
            result += cmd_desc['desc']
            result += "\n"
        return result

    def say_hello(self):
        """
        用来测试的函数
        :return: 返回第二个参数
        """
        if len(self.cmdList) == 2: return "%s: SAY_HELLO -> %s" % (datetime.datetime.now(), self.cmdList[1])
        return "%s: SAY_HELLO" % datetime.datetime.now()

    def set_auto_response_status(self):
        """
        设置全局自动回复开关
        :return: 返回设置完以后的值
        """
        if len(self.cmdList) == 2:
            if self.cmdList[1] in ['1', 'yes', 'Yes', 'YES', 'true', 'True', 'TRUE']:
                self.wechatRobotController.global_auto_response = True
                str_log = "%s: SET_AUTO_RESPONSE_STATUS -> True" % datetime.datetime.now()
                Szc_Log.debug(str_log)
                return str_log
            else:
                self.wechatRobotController.global_auto_response = False
                str_log = "%s: SET_AUTO_RESPONSE_STATUS -> False" % datetime.datetime.now()
                Szc_Log.debug(str_log)
                return str_log

    def get_auto_response_status(self):
        """
        获取当前全局自动回复状态
        :return: 返回当前是否自动回复
        """
        if self.wechatRobotController.global_auto_response: return "%s: GET_AUTO_RESPONSE_STATUS -> True" % datetime.datetime.now()
        return "%s: GET_AUTO_RESPONSE_STATUS -> False" % datetime.datetime.now()

    def start_csu_rjxy_notify(self):
        """
        开启学院通知
        1.将wechatRobotController.csu_rjxy_notify设置为True
        2.扫描mysql,如果有新的通知,则直接发送到班群
        :return:
        """
        if self.wechatRobotController.csu_rjxy_notify is False:
            self.wechatRobotController.csu_rjxy_notify = True
            scan_mysql_for_notify = ScanMysqlForNotify.ScanMysqlForNotify(self.wechatRobotController)
            thread.start_new_thread(scan_mysql_for_notify.start_scan, ())
            str_log = "%s: START_CSU_RJXY_NOTIFY 通知开启成功,每15分钟扫描一次" % datetime.datetime.now()
            Szc_Log.debug(str_log)
            return str_log
        else:
            str_log = "%s: START_CSU_RJXY_NOTIFY 通知已经开启,请勿重新开始" % datetime.datetime.now()
            Szc_Log.debug(str_log)
            return str_log

    def stop_csu_rjxy_notify(self):
        """
        关闭学院通知
        依然通过wechatRobotController.csu_rjxy_notify控制
        :return:
        """
        self.wechatRobotController.csu_rjxy_notify = False
        str_log = "%s: FINISH_CSU_RJXY_NOTIFY 通知关闭成功" % datetime.datetime.now()
        Szc_Log.debug(str_log)
        return str_log

    def get_csu_rjxy_notify_status(self):
        """
        获得学院通知状态
        :return:
        """
        return "True" if self.wechatRobotController.csu_rjxy_notify else "False"
