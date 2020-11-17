# -*- coding: utf-8 -*-
# @Time : 2020/7/7 5:51
# @Author : MYH
# @File : 7.2 PIL库的使用.py
# @Software: PyCharm

# PIL库是Python语言的第三方库,需要通过pip方式进行安装 安装库的名字叫pillow
# PIL库支持图像存储/显示/处理 能够处理几乎所有格式 可以完成对图像的一系列处理 PIL库主要可以实现图像归档和图像处理两方面需求
# 图像归档: 对图像进行批处理,生成图像预览,图像格式转换等
# 图像处理: 图像的基本处理,图像像素处理,颜色处理等
# 主要介绍PIL库中常用的3个子库: Image ImageFilter ImageEnhance

# 在PIL中任何图片都可以使用Image来表示 其方法有:
# Image.open(filename) 根据参数加载图片文件
# Image.new(mode,size,color) 根据给定参数值创建一个图像
# Image.open(StringIO.StringIO(buffer)) 从字符串中获取图像
# Image.frombytes(mode,size,data) 根据像素点data创建图像
# Image.verify() 对文件完整性进行检查,返回异常

# from PIL import Image

# 读取文件
# image = Image.open("file/bmp.bmp", 'r')

# Image.format 标识图像格式或者来源 如果图像不是从文件读取则返回None
# Image.mode 色彩的图像模式  L:灰度 RGB:彩色 CMYK:出版图像
# Image.size 图像的宽度和高度 返回值是二元元组
# Image.palette 调色板属性 返回一个ImagePalette属性

# print(image.format, image.mode, image.size, image.palette)  # 打印输出

# CMYK色彩是印刷时采用的一套色彩体系(印刷四色) 利用色料的三原色和黑色墨油混合叠加,形成各种色彩
# C是青色 M是品红 Y是黄色 K是定位套版色(黑色)

# Image类型还可以读取序列类图像文件 使用open可以打开第一帧,使用seek和tell可以在 帧之间进行切换 方法有:
# Image.seek(frame)   跳转到指定帧
# Image.tell()        返回当前帧的帧序号

# 提取GIF动画中的每一帧保存成一个文件
# image = Image.open("file/gif.gif", 'r')
# try:
#     image.save('file/picframe{:02d}.png'.format(image.tell()))
#     while True:
#         image.seek(image.tell() + 1)
#         image.save('file/picframe{:02d}.png'.format(image.tell()))
# except:
#     print("处理结束")

# 图像的转换和保存方法
# Image.save(filename, format)  # 图像保存为filename,图片格式为format
# Image.convert(mode)  # 使用不同的参数,转换图像为新的模式
# Image.thumbnail(size)  # 创建图像(大小为size)的缩略图 生成副本
# Image类还可以缩放图像以及进行旋转操作
# Image.resize(size)  # 按照size大小进行缩放,生成副本
# Image.rotate(angle)  # 按照角度旋转图片,生成副本

# image = Image.open("file/picframe00.png")  # 打开的时候要写Image.open 否则后面的save会出错
# image.save("file/picframe00.bmp")  # png格式不能转换称jpg格式
# image.thumbnail((128, 128))  # 传进去要是一个元组 转换称缩略图
# image.save("file/frame.png")  # 缩略图进行存储
# image.resize((256,512))
# image.save("file/picframe_resize.png")
# image.rotate(90)
# image.save("file/picframe_rotate.png")
# image.close()

# Image类的图像像素和通道处理方法
# Image.point(func)  # 根据函数func对每一个元素进行运算,返回图像副本
# Image.split()  # 提取RGB图像的每一个颜色通道,返回图像副本
# Image.merge(mode, bands)  # 合并通道,其中mode表示色彩,bands表示色彩通道
# Image.blend(im1, im2, alpha)  # 两幅图片进行公式插值形成新的图片 im1*(1.0-alpha)+im2*alpha

# im1 =Image.open("file/piccc.jpg")
# r,g,b = im1.split()
# om = Image.merge("RGB",(r,g,b))
# om.save("file/pieee.jpg")

# 如果需要对每一个像素点进行操作则需要使用到lambda函数
# im1 = Image.open("file/piccc.jpg")  # 打开文件
# r, g, b = im1.split()  # 进行像素分离 形成r g b 三个变量
# newr = r.point(lambda i: i * 0.9)  # 进行R像素的处理
# newg = g.point(lambda i: i * 1.9)  # 进行G像素的处理
# newb = b.point(lambda i: i * 3.9)  # 进行B像素的处理
# out = Image.merge(om.mode, (newr, newg, newb))  # 形成一张新的图片
# out.save("file/savedimage.png")  # 对新的图片进行保存

# 图像的过滤和增强
# PIL库中的ImageFileter类和ImageEnhance类提供了过滤图像和增强图像的方法
# ImageFilter类提供了10中图像处理的方法:
# ImageFilter.BLUR  # 图像的模糊效果
# ImageFilter.CONTOUR  # 图像的轮廓效果
# ImageFilter.DETAIL  # 图像的细节效果
# ImageFilter.EDGE_ENHANCE  # 图像的边界增强效果
# ImageFilter.EDGE_ENHANCE_MORE  # 图像的阈值边界增强效果
# ImageFilter.EMBOSS  # 图像的浮雕效果
# ImageFilter.FIND_EDGES  # 图像的边界效果
# ImageFilter.SMOOTH  # 图像的平滑效果
# ImageFilter.SMOOTH_MORE  # 图像的阈值平滑效果
# ImageFilter.SHARPEN  # 图像的锐化效果

from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

# im = Image.open("file/flower.jpg")
# om = im.filter(ImageFilter.BLUR)
# om.save("file/savedFilter01.jpg")
# om = im.filter(ImageFilter.CONTOUR)
# om.save("file/savedFilter02.jpg")
# om = im.filter(ImageFilter.DETAIL)
# om.save("file/savedFilter03.jpg")
# om = im.filter(ImageFilter.EDGE_ENHANCE)
# om.save("file/savedFilter04.jpg")
# om = im.filter(ImageFilter.EDGE_ENHANCE_MORE)
# om.save("file/savedFilter05.jpg")
# om = im.filter(ImageFilter.EMBOSS)
# om.save("file/savedFilter06.jpg")
# om = im.filter(ImageFilter.FIND_EDGES)
# om.save("file/savedFilter07.jpg")
# om = im.filter(ImageFilter.SMOOTH)
# om.save("file/savedFilter08.jpg")
# om = im.filter(ImageFilter.SMOOTH_MORE)
# om.save("file/savedFilter09.jpg")
# om = im.filter(ImageFilter.SHARPEN)
# om.save("file/savedFilter10.jpg")


# ImageEnhance类提供的图像增强和滤镜的方法
# ImageEnhance.enhance(factor)  # 对选择属性的数值增强factor倍
# ImageEnhance.Color(im)  # 调整对象的颜色平衡
# ImageEnhance.Contrast(im)  # 调整图像的对比度
# ImageEnhance.Brightness(im)  # 调整图像的亮度
# ImageEnhance.Sharpness(im)  # 调整图像的锐度

# im = Image.open("file/savedFilter01.jpg")
# om = ImageEnhance.Contrast(im)
# om.enhance(90).save("file/savedEnhance01.jpg")
# om = ImageEnhance.Color(im)  # 获取颜色平衡
# om.enhance(90).save("file/savedEnhance02.jpg")
# om = ImageEnhance.Sharpness(im)  # 获取锐度
# om.enhance(90).save("file/savedEnhance03.jpg")
# om = ImageEnhance.Brightness(im)  # 获取亮度
# om.enhance(90).save("file/savedEnhance04.jpg")
