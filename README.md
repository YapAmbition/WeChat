Wechat微信机器人
===

### 改动日志

* 2018-02-15 通过给自己发送指令，控制机器人的开关，以防两个机器人无限发消息或者和别人谈正事时机器人出来捣乱

* 2018-02-18 添加日志模块 Szc_Log

* 2018-04-11 大幅度修改机器人逻辑,留下了机器人的核心功能:自动回复(默认关闭),与学院信息网爬虫共同组建了院内新通知直接发群里的逻辑

### 2018-04-11

* 将微信机器人的核心部分放入一个文件(WechatRobot.py):注册消息,发送消息,由于注册消息在itchat中是阻塞式的,所以响应式发送消息都需要新建线程进行发送(注意)

* 机器人的所有功能通过一个类的成员变量来进行控制:WechatRobotController.py

* 机器人的所有命令模式通过WechatRobotCommand.py进行扩展和修改

* 需要扩展机器人功能时,需要在WechatRobotController.py中添加控制的成员变量进行控制,然后在WechatRobotCommand.py中进行逻辑编写,对于持续性功能需要新建线程执行

* 该机器人与院网爬虫共同组成院网新消息通知系统:[院网爬虫](https://github.com/YapAmbition/csu_rjxy_notify "https://github.com/YapAmbition/csu_rjxy_notify")

### 最后的改动 2018-04-12

* 由于费老师讲群名字改了,所以需要修改代码(由于开始时并不希望将过多的功能交付给命令模式,所以还是用修改代码的方式来应对群名字的改变)

#### TODO

* Szc_Log暂时没用到,但是为了软件的健壮性,还是需要在后期添加日志排查可能出现的错误

* 需要添加一个命令能够查询当前机器人正在做什么:是否开启自动回复,是否开启学院通知

* 需要添加一个命令能够查询机器人能够做什么,类似于linux -help帮助

* 群聊列表不完整的现象还没改变