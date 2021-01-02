# -*- coding: utf-8 -*-
# @Time : 2020/12/31 15:24
# @Author : MYH
# @File : 图像直方和均衡.py
# @Software: PyCharm

from PIL import Image
from pylab import *
from PCV.tools import imtools

from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\SimSun.ttc", size=14)

im = array(Image.open('test/test.jpg').convert('L'))
im2, cdf = imtools.histeq(im)

figure()
subplot(2, 2, 1)
axis('off')
gray()
title(u'原始图像', fontproperties=font)
imshow(im)

subplot(2, 2, 2)
axis('off')
title(u'直方图均衡化后的图像', fontproperties=font)
imshow(im2)

subplot(2, 2, 3)
axis('off')
title(u'原始直方图', fontproperties=font)
# hist(im.flatten(), 128, cumulative=True, normed=True)
hist(im.flatten(), 128, normed=True)

subplot(2, 2, 4)
axis('off')
title(u'均衡化后的直方图', fontproperties=font)
# hist(im2.flatten(), 128, cumulative=True, normed=True)
hist(im2.flatten(), 128, normed=True)

show()