'''
    @Time : 2020/5/26 11:55 
    @Author : Mao Yuhuan
    @FileName : 2.7 六角星的绘制
    @Software: PyCharm
'''


import turtle

def draw_a_triangle(angle):
    turtle.seth(0+angle)
    turtle.fd(200)
    turtle.seth(120+angle)
    turtle.fd(200)
    turtle.seth(240+angle)
    turtle.fd(200)


turtle.width(6)
draw_a_triangle(0)
turtle.pu()
turtle.seth(60)
turtle.fd(66.6)
turtle.seth(120)
turtle.fd(66.6)
turtle.pd()
draw_a_triangle(-60)

turtle.done()