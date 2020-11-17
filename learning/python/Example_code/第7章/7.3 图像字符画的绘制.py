# -*- coding: utf-8 -*-
# @Time : 2020/7/8 18:48
# @Author : MYH
# @File : 7.3 图像字符画的绘制.py
# @Software: PyCharm

# 导入部分
from PIL import Image

# 采用字符串替代像素,则图像就变成了字符画
# 自定义一个符号列表
ascii_char = list('"$%_&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-/+@<>i!;:,\^`.')


# 灰度值从高到低依次使用list中的元素
# 可以使用灰度值,将彩色图像转换为高质量的黑白文档,灰度值值图像中颜色深度,白色为255,黑色为0
# 定义彩色转换成灰度的公式是: R * 0.2126 + G * 0.7152 + B * 0.0722

def get_char(R, B, G, alpha=256):
    if alpha == 0:
        return ' '
    print(R, G, B, alpha, len(ascii_char))
    gray = int(R * 0.2126 + G * 0.7152 + B * 0.0722)  # 计算灰度值
    unit = 256 / len(ascii_char)  # 计算每一个等级
    print(gray // unit)
    return ascii_char[int(gray // unit)]


# 为了使生成的字符画有最佳效果,可以使用resize(size)重新设定图像大小 这里是对像素在新的尺寸下进行重新排列
# 可以使用创建一个新的字符串txt 使用嵌套循环添加字符,使用im.getpixel() 方法可以返回给定图像位置的像素值.如果图像为多通道,则返回一个RGB元组

def main():
    im = Image.open("file/savedEnhance04.jpg")  # 打开图像
    WIDTH, HEIGHT = 100, 60  # 设定宽高
    im = im.resize((WIDTH, HEIGHT))  # 重设图像大小
    txt = ""  # 创建一个空文本
    for height in range(HEIGHT):
        for width in range(WIDTH):
            txt += get_char(*im.getpixel((width, height)))  # 遍历,获取到每一个灰度值对应的字符并写入txt *是元组拆分操作
        txt += '\n'  # 一行结束换一行
    fo = open("file/pic_char.txt", "w")  # 新建文本文件
    fo.write(txt)  # 写入字符串
    fo.close()  # 关闭文件


main()

# from PIL import Image
#
# ascii_char = list('"$%_&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-/+@<>i!;:,\^`.')
#
#
# def get_char(r, b, g, alpha=256):
#     if alpha == 0:
#         return ' '
#     gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
#     unit = 256 / len(ascii_char)
#     return ascii_char[int(gray // unit)]
#
#
# def main():
#     im = Image.open('file/piddd.jpg')
#     WIDTH, HEIGHT = 100, 60
#     im = im.resize((WIDTH, HEIGHT))
#     txt = ""
#     for i in range(HEIGHT):
#         for j in range(WIDTH):
#             txt += get_char(*im.getpixel((j, i)))
#         txt += '\n'
#     fo = open("pic_char.txt", "w")
#     fo.write(txt)
#     fo.close()
#
#
# main()
