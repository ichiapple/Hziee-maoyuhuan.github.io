'''
    @Time : 2020/5/26 11:50 
    @Author : Mao Yuhuan
    @FileName : 2.6 无角正方形的绘制
    @Software: PyCharm
'''

import turtle


def forward_line():
    turtle.pu()
    turtle.fd(100)
    turtle.pd()
    turtle.fd(100)
    turtle.pu()
    turtle.fd(100)


turtle.width(10)
forward_line()
turtle.seth(90)
forward_line()
turtle.seth(180)
forward_line()
turtle.seth(-90)
forward_line()
turtle.done()

