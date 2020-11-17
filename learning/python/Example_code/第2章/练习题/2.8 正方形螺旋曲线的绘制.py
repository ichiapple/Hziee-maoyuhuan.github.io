'''
    @Time : 2020/5/26 12:15 
    @Author : Mao Yuhuan
    @FileName : 2.8 正方形螺旋曲线的绘制
    @Software: PyCharm
'''
import turtle


def draw_a_rectangle(r):
    turtle.seth(90)
    turtle.fd(r)
    turtle.seth(180)
    turtle.fd(r)
    turtle.seth(270)
    turtle.fd(r + 10)
    turtle.seth(0)
    turtle.fd(r + 10)


turtle.width(4)
for i in range(30):
    draw_a_rectangle(20 * i + 10)

turtle.done()

# draw_a_rectangle(10)
# draw_a_rectangle(30)
# draw_a_rectangle(50)
