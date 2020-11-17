'''
    @Time : 2020/5/26 11:41 
    @Author : Mao Yuhuan
    @FileName : 2.3 绘制彩色蟒蛇
    @Software: PyCharm
'''

import turtle

turtle.setup(800, 500, 500, 300)
colors = ['red','green','yellow','purple']
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.seth(-40)
for i in range(4):
    turtle.color(colors[i])
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80 / 2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2 / 3)
turtle.done()
