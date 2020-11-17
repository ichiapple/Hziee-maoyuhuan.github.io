'''
    @Time : 2020/5/25 18:31 
    @Author : Mao Yuhuan
    @FileName : 2.3 绘制一个包含9个同心圆的靶子
    @Software: PyCharm
'''

import turtle


def change_position():
    turtle.penup()
    turtle.seth(-90)
    turtle.forward(20)
    turtle.seth(0)
    turtle.pendown()


turtle.width(5)
for i in range(1, 10):
    turtle.circle(i * 20)
    change_position()

turtle.done()
