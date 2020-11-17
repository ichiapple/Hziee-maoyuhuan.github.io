'''
    @Time : 2020/5/25 12:18 
    @Author : Mao Yuhuan
    @FileName : 2.3 Python绘制蟒蛇
    @Software: PyCharm
'''
# 导入画图库
import turtle

# 设置画布
# 函数参数为 width, height, startX, startY 设置窗体的大小和位置
# width 如果为整数则为像素值 如果为小数则为窗口宽度和屏幕的比例
# height 如果为整数则为像素值 如果为小数则为窗口宽度和屏幕的比例
# startX 窗口左侧与屏幕左侧的像素距离 如果为null则水平居中
# startY 窗口顶部与屏幕顶部的像素距离 如果为null则竖直居中
turtle.setup(800, 500, 500, 300)

# 笔抬起
# penup和pendown为画笔控制函数 可以缩写为pd和pu
turtle.penup()
# 移动
turtle.fd(-250)
# 笔落下
turtle.pendown()
# 设置笔触大小
# turtle.pensize(width) 也可以写成turtle.width(width) 如果不加参数返回当前的笔触大小
turtle.pensize(25)
# 设置笔触颜色
# turtle.color(color) 也可以写成turtle((r, g, b))
turtle.color("green")
# 设置画笔绘制方向
# turtle.seth(to_angle)
turtle.seth(-40)
# 循环画出蛇的身体
# 使用循环进行绘画蛇的身体
# turtle.circle(radius, extent=None)  radius是半径 extent为角度 不设置则绘画整个圆
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
# 回正方向
turtle.circle(40, 80 / 2)
# 往前画一段距离
# turtle.forward(distance) 也可写成 turtle.fd(distance)
turtle.fd(40)
# 画一个半圆
turtle.circle(16, 180)
# 再往回画大半个蛇头
turtle.fd(40 * 2 / 3)

# 可以使用函数封装思想进行函数的封装


