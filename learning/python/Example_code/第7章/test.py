# -*- coding: utf-8 -*-
# @Time : 2020/7/9 1:31
# @Author : MYH
# @File : test.py
# @Software: PyCharm

from PIL import Image  # 引入PIL库


def get_gray(R, G, B):  # 计算返回对应rgb值下的灰度值
    return R * 0.2126 + G * 0.7152 + B * 0.0722


def main():
    im = Image.open("file/cw.jpg")  # 打开图像
    # print(im.size)  # 获得图像的宽高
    WIDTH, HEIGHT = im.size[0], im.size[1]  # 设定宽高
    om = im.resize((WIDTH, HEIGHT))  # 重设图像大小
    for height in range(HEIGHT):  # 用双层循环对每一个像素点进行遍历
        for width in range(WIDTH):
            pix = im.getpixel((width, height))  # 获取每一个像素点
            if get_gray(pix[0], pix[1], pix[2]) > 160:  # 判断像素点灰度值是否大于阈值 如果大于则为黑色 否则为白色
                om.putpixel([width, height], (0, 0, 0))
            else:
                om.putpixel([width, height], (255, 255, 255))
    om.save("file/cwj.bmp")  # 输出图像 设定图像名


main()  # 执行main函数
