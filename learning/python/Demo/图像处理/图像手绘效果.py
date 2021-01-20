# -*- coding: utf-8 -*-
# @Time : 2020/12/30 22:13
# @Author : MYH
# @File : 图像手绘效果.py
# @Software: PyCharm

from PIL import Image
import numpy as np

vec_el = np.pi / 2.2  # 光源的俯视角度 弧度制
vec_az = np.pi / 4.  # 光源的方位角度 弧度制
depth = 10.  # (0-100) 深度值
im = Image.open("test/test.jpg").convert("L")  # 打开图像并进行转换
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
im2.save("test/testSavedImg.png")
im2.show()
