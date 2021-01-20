# -*- coding: utf-8 -*-
# @Time : 2020/12/30 23:48
# @Author : MYH
# @File : 图像基本处理.py
# @Software: PyCharm

from PIL import Image, ImageFilter, ImageEnhance, ImageDraw, ImageFont

img = Image.open("test/test.jpg")
print(img)  # 得到图像基本信息 image mode=RGB size=640x321
print(img.format)  # 得到图像的文件格式
print(img.mode)  # 图像色彩格式 L->灰度图像 RGB->真彩色图像 CMYK->出版图像
print(img.size)  # 图像大小

img1 = img.resize((1500, 700))  # 图片简单进行拉伸
print(img1.size)
# img1.show()  # 展示图像

img2 = img1.rotate(45)  # 逆时针进行旋转 多的部分会进行剪裁
# img2.show()

img3 = img.convert('L')  # 转换成灰度图 色彩模式转换
# img3.show()

img4 = img.filter(ImageFilter.CONTOUR)  # 画出图像轮廓
# img4.show()

img5 = ImageEnhance.Contrast(img).enhance(5)  # 修改对比度 默认对比度为1
# img5.show()

img6 = img.transpose(Image.FLIP_LEFT_RIGHT)  # 左右反转
# img6.show()
img7 = img.transpose(Image.FLIP_TOP_BOTTOM)  # 上下反转
# img7.show()

size = (120, 120)  # 限制在这个大小内
img8 = img.copy()
img8.thumbnail(size)
# img8.show()

color = "rgb(255,90,90)"  # 文字颜色
img9 = img.copy()
drawImage = ImageDraw.Draw(img9)  # 加载要写文字的图片
font = ImageFont.truetype("msyhl.ttc", size=80)  # 加载字体
drawImage.text((50, 50), "Hello World", fill=color, font=font)  # 写上文字 参数分别为坐标 文本 颜色 字体
# img9.show()
