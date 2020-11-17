'''
    @Time : 2020/5/26 12:27 
    @Author : Mao Yuhuan
    @FileName : 2.9 自定义蟒蛇
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
    turtle.circle(40, 60)
    turtle.circle(-40, 60)
turtle.circle(40, 60 / 2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2 / 3)
turtle.circle(-40, 150)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2 / 3)
turtle.done()