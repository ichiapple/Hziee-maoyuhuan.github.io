# -*- coding: utf-8 -*-
# @Time : 2020/12/31 15:15
# @Author : MYH
# @File : 图像灰度处理.py
# @Software: PyCharm

from PIL import Image
from pylab import *
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"c:\windows\fonts\SimSun.ttc", size=14)  # 设置字体
pil_im = Image.open('test/test.jpg')  # 打开文件
print(pil_im.mode, pil_im.size, pil_im.format)  # 打印图片颜色格式 图片大小 图片格式
subplot(121)  # 设置展示格式 1行2列位于第一个位置

title(u'原图', fontproperties=font)
axis('off')
imshow(pil_im)

pil_im = Image.open('test/test.jpg').convert('L')
gray()
subplot(122)  # 1行2列位于第二个位置
title(u'灰度图', fontproperties=font)
axis('off')
imshow(pil_im)
show()
