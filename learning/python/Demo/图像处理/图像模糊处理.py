# -*- coding: utf-8 -*-
# @Time : 2020/12/30 22:17
# @Author : MYH
# @File : 图像模糊处理.py
# @Software: PyCharm

from PIL import Image, ImageFilter

# 加载图像
picture = Image.open('test/test.jpg')

# 进行图像处理
picture2 = picture.filter(ImageFilter.BLUR)
picture2.save("test/testSavedImgBlur.jpg","jpeg")
picture2.show()

picture3 = picture.filter(ImageFilter.GaussianBlur(radius=5))
picture3.save("test/testSavedImgBlur2.jpg","jpeg")
picture3.show()


