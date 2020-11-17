# -*- coding: utf-8 -*-
# @Time : 2020/7/3 17:27
# @Author : MYH
# @File : 4.6 pai的计算.py
# @Software: PyCharm

# Π是一个无理数,同时也是一个无限不循环小数是很多学科的关键
# 求解Π可以使用BBP公式 随着计算机的发现,还可以 使用蒙特卡罗方法(又称随机抽样/统计实验方法)
# 求解方法:   输入: 抛点数 处理: 计算点到圆心的距离,统计在圆内点的数量 输出:Π值

from random import random, seed
from math import sqrt
from time import clock

darts = 10000  # 抛点数 越大越精准但是花费时间越长
hits = 0.0  # 在圆内数 为了方便除操作 故定义为浮点数
clock()  # 启动定时器 用于和后面的定时器进行时间差的计算 clock()不建议使用 会报警告
for i in range(1, darts + 1):
    # seed(265)  # 如果在每次进行随机数生成之前进行seed值的设定,则每次计算的结果都是一样的
    x, y = random(), random()
    dist = sqrt(x ** 2 + y ** 2)
    if dist < 1.0:
        hits += 1
pi = 4 * (hits / darts)
print("Pi的值为:{}".format(pi))
print("运行时间为:{:.4f}".format(clock()))
