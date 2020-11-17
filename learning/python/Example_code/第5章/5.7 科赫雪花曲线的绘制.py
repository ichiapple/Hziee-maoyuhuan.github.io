# -*- coding: utf-8 -*-
# @Time : 2020/7/4 3:00
# @Author : MYH
# @File : 5.7 科赫雪花曲线的绘制.py
# @Software: PyCharm

# 绘制方法: 正整数n代表曲线的 阶数,表示生成曲线的 操作次数
# 0阶曲线是一条长度为L的线段 等分为三段,中间一段使用等边三角形进行替换得到1阶科赫曲线 同理重复则可以得到n阶的科赫曲线

import turtle


def koc(size, n):
    if n == 0:  # 0阶就是一条对应size的直线
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koc(size / 3, n - 1)  # 分三段 绘制n-1阶科赫曲线


def main():
    turtle.setup(900, 500)  # 设置画布大小
    turtle.speed(4)  # 控制绘制速度
    turtle.pu()  # 笔抬起
    turtle.goto(-400, -60)  # 移动位置到曲线开始的地方
    turtle.pd()  # 笔放下
    turtle.pensize(2)
    koc(800, 4)
    turtle.hideturtle()
    turtle.done()


# 绘制一条科赫曲线
# main()

def main2():
    turtle.setup(600, 600)
    turtle.speed(0)
    turtle.pensize(2)
    turtle.pu()
    turtle.goto(-200, 100)
    turtle.pd()
    level = 4
    size = 400
    koc(size, level)  # 绘制了前面那个例子三次 每次旋转一个120°
    turtle.right(120)
    koc(size, level)
    turtle.right(120)
    koc(size, level)
    turtle.hideturtle()
    turtle.done()


# 绘制科赫雪花
# main2()


def koc_1(size, n):
    if n == 0:  # 0阶就是一条对应size的直线
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.right(angle)
            koc_1(size / 3, n - 1)  # 分三段 绘制n-1阶科赫曲线


def main3():
    turtle.setup(900, 500)  # 设置画布大小
    turtle.speed(4)  # 控制绘制速度
    turtle.pu()  # 笔抬起
    turtle.goto(-400, 100)  # 移动位置到曲线开始的地方
    turtle.pd()  # 笔放下
    turtle.pensize(2)
    koc_1(800, 4)
    turtle.hideturtle()
    turtle.done()


# main3()


def main4():
    turtle.setup(900, 500)  # 设置画布大小
    turtle.speed(4)  # 控制绘制速度
    turtle.pu()  # 笔抬起
    turtle.goto(-400, -60)  # 移动位置到曲线开始的地方
    turtle.pd()  # 笔放下
    turtle.pencolor("green")
    turtle.pensize(2)
    koc(800, 4)
    turtle.hideturtle()
    turtle.done()


main4()
