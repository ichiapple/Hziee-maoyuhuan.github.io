# -*- coding: utf-8 -*-
# @Time : 2020/7/4 2:02
# @Author : MYH
# @File : 5.4 七段数码管的绘制.py
# @Software: PyCharm

# 数码管能够实现2**7种不同状态,其中部分是人们能够理解的数字/字符
import datetime, turtle


def drawLine(draw):
    turtle.pd() if draw else turtle.pu()  # 如果需要画则按下画笔,否则抬起
    turtle.fd(40)
    turtle.right(90)


def drawDigit(d):  # 根据数字的显示,绘制七段数码管 一段一段来的
    drawLine(True) if d in [2, 3, 4, 5, 6, 8, 9] else drawLine(False) # s=使用单行的if-else使代码更加紧凑
    drawLine(True) if d in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 2, 6, 8] else drawLine(False)
    turtle.left(90)  # 上一行代码执行完毕方向是指向0°方向,所以需要向上画则需要左转90°
    drawLine(True) if d in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
    turtle.pu()  # 抬起画笔
    turtle.left(180)  # 转向
    turtle.fd(20)  # 间隔为20


def drawDate(date):
    for i in date:
        drawDigit(eval(i))  # 通过eval函数能将字符串转换为一个数字


def main():
    turtle.setup(950, 350, 200, 200)
    turtle.pu()
    turtle.fd(-400)
    turtle.pensize(5)  # 设置笔触的大小
    drawDate(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
    turtle.hideturtle()  # 隐藏tutle笔触
    turtle.done()


main()
