#!/usr/bin/python
# ! -*-coding:utf-8 -*-
"""
每隔半小时扫描mysql,观察是否有通知更新,如果有则直接发送给班群
"""

import MySQLdb
import time
import WechatRobot
import datetime
import Szc_Log


class ScanMysqlForNotify:

    def __init__(self, wechat_robot_controller):
        self.host = "localhost"
        self.username = "root"
        self.password = "954552106"
        self.database = "csu_rjxy_notify"
        self.table_name = "informations"
        self.interval = int(60 * 15)  # 扫描时间间隔15分钟
        self.wechatRobotController = wechat_robot_controller

    def start_scan(self):
        """
        连接mysql并扫描查看是否有新的通知,如果有则发送至班群并更新数据库表
        :return:
        """
        db = MySQLdb.connect(self.host, self.username, self.password, self.database, use_unicode=True, charset="utf8")
        cursor = db.cursor()
        scan_sql = "SELECT * FROM %s WHERE `is_new` = 1" % self.table_name
        while self.wechatRobotController.csu_rjxy_notify:
            cursor.execute(scan_sql)
            informations = cursor.fetchall()
            str_log = "%s: scan mysql : %s" % (datetime.datetime.now(), str(informations))
            Szc_Log.debug(str_log)
            if len(informations) > 0:
                for information in informations:
                    WechatRobot.say_to_1406(format_information(information))
                    update_sql = "UPDATE %s SET `is_new` = 0 WHERE id = %d" % (self.table_name, information[0])
                    cursor.execute(update_sql)
                db.commit()
            time.sleep(self.interval)
        db.close()


def format_information(information):
    """
    格式化通知,等待微信端输出
    :param information: 从mysql获取到的一条通知
    :return:
    """
    notify = "院网又发通知啦:\n标题: %s\n连接: %s\n日期: %s" % (information[1], information[2], information[3])
    return notify

