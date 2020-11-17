# -*- coding: utf-8 -*-
# @Time : 2020/7/4 1:33
# @Author : MYH
# @File : 5.3 datetime库的应用.py
# @Software: PyCharm

# datetime库提供了一个处理时间的标准库 提供了一系列的事件处理的方法 可以从系统中获取时间并按照一定的格式进行输出
# from datetime import *

# datetime.datetime.date  # 表示日期类 有年月日
# datetime.time  # 表示时间类 有时分秒
# datetime.datetime  # 表示日期和时间 包含了前面两类
# datetime.timedelta  # 主要介绍 与时间的间隔有关
# datetime.tzinfo  # 与时区有关的信息

from datetime import datetime

today = datetime.now()  # 获取当前的系统时间
print(today)  # 打印当前时间
today = datetime.utcnow()  # 获取当前的世界标准时间/UTC时间
print(today)

defineADay = datetime(2019, 9, 6, 12, 6, 45, 56432)  # 传入参数是 年 月 日 时 分 秒 毫秒 用于构造一个时间
print(defineADay)

# 对defineADay的一些基本操作
print(defineADay.min)  # 能表示的最小时间
print(defineADay.max)  # 能表示的最大时间
print(defineADay.year)  # 当前表示时间的年
print(defineADay.month)  # 当前表示时间的月
print(defineADay.day)  # 当前表示时间的日
print(defineADay.hour)  # 当前表示时间的时
print(defineADay.minute)  # 当前表示时间的分
print(defineADay.second)  # 当前表示时间的秒
print(defineADay.microsecond)  # 当前表示时间的毫秒

# 格式化的方法
print(defineADay.isoformat())  # 采用ISO8601进行时间格式化显示(日期和时间之间有T表示)
print(defineADay.isoweekday())  # 根据日期计算返回一个1-7的数表示是周几
print(defineADay.strftime("%Y-%m-%d %H:%M:%S"))  # 根据格式化字符串format进行格式的显示
# %Y年 %m月 %d日 %H时 %M分 %S秒 %B月名 %b月名缩写 %A星期 %a星期缩写 %x日期 %X时间 以下是演示
print(defineADay.strftime('%Y') + "年\t" +
      defineADay.strftime('%m') + "月\t" +
      defineADay.strftime('%d') + "日\t" +
      defineADay.strftime('%H') + "时\t" +
      defineADay.strftime('%M') + "分\t" +
      defineADay.strftime('%S') + "秒\t" +
      defineADay.strftime('%B') + "月\t" +
      defineADay.strftime('%b') + "缩写月名\t" +
      defineADay.strftime('%A') + "星期\t" +
      defineADay.strftime('%a') + "缩写星期\t" +
      defineADay.strftime('%x') + "日期\t" +
      defineADay.strftime('%X') + "时间\t")
now =datetime.now()
print("现在是的{0:%Y}年{0:%m}月{0:%d}日{0:%H}时{0:%M}分{0:%S}秒".format(now))
