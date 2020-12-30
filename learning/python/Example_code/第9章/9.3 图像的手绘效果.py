# -*- coding: utf-8 -*-
# @Time : 2020/7/10 0:33
# @Author : MYH
# @File : 9.3 图像的手绘效果.py
# @Software: PyCharm

# 导入部分
from PIL import Image
import numpy as np

# im = np.array(Image.open('file/pic.png'))
# print(im.shape, im.dtype)  # (673, 681, 3) uint8 分别为shape和类型 图像转换的是一个三位数据 分别为宽/高/像素点的RGB值 每一个RGB值是一个单字节整数

# PIL库中由图像转换函数,能够改变图像单个像素的表示形式 使用convert()/'L'模式可以将RGB值变成一个单一数值模式 图像从彩色变成灰度黑白图像
# pic = Image.open('file/pic.png').convert('L')
# im = np.array(pic)
# pic.save("file/bb.png")
# print(im.shape, im.dtype)  # 变为二维数组,每个像素点由一个二维数据进行表示

# 同时也可以获取像素值以及像素最大和最小值
# print(im[20, 200], int(im.max()), im.min())
# print(im)  # 数据太多会用...进行缩写
# print(im[10, :])  # 写法参照https://blog.csdn.net/Dongfnag_HU/article/details/92620865
# print(im[10])  # 和上面一样 把第十行取出来

# 将图像读入ndarray数组后,可以通过任意数学操作对其进行变换 值得注意: 某些操作会改变数据类型,需要使用numpy.uint()变化成整数
# im1 = 255 - im  # 反变换
# im2 = (100 / 255) * im + 150  # 区间变换
# im3 = 255 * (im1 / 255) ** 20  # 像素平方处理
# pil_im = Image.fromarray(np.uint(im1))
# pil_im.show()  # 这里是使用系统图片浏览器进行展示 储存出问题
# # pil_im.save("file/im1.png") # 出问题
# pil_im = Image.fromarray(np.uint(im2))
# pil_im.show()
# pil_im = Image.fromarray(np.uint(im3))
# pil_im.show()

# 灰度值: 灰度值是指黑白图像中点的颜色深度, 从0到255, 黑为0, 白为255, 一般用于构造非可见光图像(超声波图像等) 一般用于计算机计算能力不充分形成图像
# 其中灰度值可以通过RGB进行转换, 公式为: Gray = 0.3 * R + 0.59 * G + 0.11 * B

# 图像的手绘效果
# 灰度从直观上来看就是颜色梯度, 通常可以通过梯度提取颜色轮廓
# numpy中提供了方法gradient(), 传入图像数组即可返回代表x和y各自方向上的梯度变化的二维数组

# 定义了方位角和俯视角和深度权值,角度设定和单位向量构成了基础坐标系 用三维立体考虑问题
vec_el = np.pi / 2.2  # 光源的俯视角度 弧度制
vec_az = np.pi / 4.  # 光源的方位角度 弧度制
depth = 10.  # (0-100) 深度值
im = Image.open("file/muke.jpg").convert("L")  # 打开图像并进行转换
a = np.asarray(im).astype(float)  # 转换为一个浮点型的数组
grad = np.gradient(a)  # 取图像的灰度梯度值
grad_x, grad_y = grad  # 分别取横向和纵向的梯度值
grad_x = grad_x * depth / 100  # 根据原x方向计算新的x方向
grad_y = grad_y * depth / 100
grad_z = 1.
dx = np.cos(vec_el) * np.cos(vec_az)  # 光源对x轴的影响 # 这三个分别是加权向量
dy = np.cos(vec_el) * np.sin(vec_az)  # 光源对y轴的影响
dz = np.sin(vec_el)  # 光源对z轴的影响
A = np.sqrt(grad_x ** 2 + grad_y ** 2 + grad_z ** 2)  # 利用每一个单元的梯度值对方向加权向量合成灰度值
uni_x = grad_x / A  # A是梯度幅值,也就是梯度大小
uni_y = grad_y / A
uni_z = grad_z / A
a2 = 255 * (uni_x * dx + uni_y * dy + uni_z * dz)  # 光源归一化
a2 = a2.clip(0, 255)  # 预防溢出
im2 = Image.fromarray(a2.astype('uint8'))  # 重构图像 从数组恢复图像并保存
im2.save("file/savedImg.png")
im2.show()

# 手绘图利用像素之间的梯度值重构每一个像素点 为体现光照效果设计了一个光源,建立光源对各店梯度值的影响函数,进而算出像素值体现边缘灰度变化,形成手绘效果
# depth值旨在调节重构图像的时候取的不同灰度值 越小越白
