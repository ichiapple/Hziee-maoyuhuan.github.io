# -*- coding: utf-8 -*-
# @Time : 2020/12/31 0:30
# @Author : MYH
# @File : 图像伪色彩增强.py
# @Software: PyCharm
import cv2

# src = cv2.imread(r"test/test.jpg")
# cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
# cv2.imshow("input", src)
# dst = cv2.applyColorMap(src, cv2.COLORMAP_COOL)
# cv2.imshow("output", dst)

#伪彩色
image = cv2.imread("test/test.jpg")
color_image = cv2.applyColorMap(image, cv2.COLORMAP_JET)
cv2.imshow("image", image)
cv2.imshow("color_image", color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
