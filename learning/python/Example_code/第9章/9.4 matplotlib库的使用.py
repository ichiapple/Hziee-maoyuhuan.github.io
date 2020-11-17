# -*- coding: utf-8 -*-
# @Time : 2020/7/10 17:40
# @Author : MYH
# @File : 9.4 matplotlib库的使用.py
# @Software: PyCharm

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# 字体: 字体是i计算机显示字符的方式 均由人工设计并采用字体库方式部署再计算机中 但是部分字体在本库中不适用
# 宋体(SimSun) 黑体(SimHei) 楷体(Kaiti) 微软雅黑(Microsoft YaHei) 隶书(LiSu)
# 仿宋(FangSong) 幼圆(YouYuan) 华文宋体(STSong) 华文黑体(STHeiti) 苹果丽中黑(Apple LiGothic Medium)
# matplotlib.rcParams['font.family'] = 'SimHei'
# matplotlib.rcParams['font.sans-serif'] = ['SimHei']

# matplotlib库概述 引用方式为: import matplotlib.pyplot as plt
# import matplotlib.pyplot as plt  # pyplot是matplotlib的一个子库

# pyplot库解析 plt子库提供了一批操作和绘图函数,每一个函数代表对图像的一个操作 采用plt.<b>()形式进行调用 b为函数名
# plt.figure(figsize=None, facecolor=None)  # 创建一个全局绘图区域
# plt.axes(rect, axisbg='w')  # 创建一个坐标系风格的子绘图区域
# plt.subplot(nrows, ncols, plot_number)  # 在全局绘图区域中创建一个子绘图区域
# plt.subplots_adjust()  # 调整子绘图区域的布局

# plt.figure(figsize=(8, 4))  # 创建并显示绘图区 绘制图像之前也可以不创建绘图区,会默认创建一个绘图区
# plt.show()  # 但是好像并没有什么用

# 默认创建的是一个参数为(111)的坐标系 axisbg为背景色,默认为白色

# plt.subplot(323)  # 本函数用于在全局绘图区域内创建子绘图区域,含义是将全局坐标系分为3行2列,并在第三分区创建坐标系
# plt.show()

# plt.axes()# 默认创建一个subplot(111)的坐标系
# 参数表示的意思为左边距 下边距 宽度 高度 如果有两个或以上,则需要考虑不重叠
# plt.axes([0.1, 0.1, 0.8, 0.8], facecolor='green')  # 其中axisbg使用会报错 使用facecolor属性进行代替
# plt.show()

# plt库读取和显示函数
# plt.legend()  # 在绘图区域放置绘图标签
# plt.show()  # 显示创建绘图对象
# plt.matshow()  # 在窗口显示数组矩阵
# plt.imshow()  # 在axes上显示图像
# plt.imsave()  # 保存数组为图像文件
# plt.imread()  # 从图像文件中读取数组

# plt库的基础图表函数
# plt.plot(x, y, color, width)  # 根据x,y绘制直线和曲线
# plt.boxplot(data, notch, positions)  # 绘制一个箱型图
# plt.bar(left, height, width, bottom)  # 绘制一个条形图
# plt.barh(bottom, width, height, left)  # 绘制一个横向条形图
# plt.polar(theta, r)  # 绘制一个极坐标图
# plt.pie(data, explode)  # 绘制饼图
# plt.psd(x, NFFT=256, pad_to, Fs)  # 绘制功率谱密度图
# plt.specgram(x, NFFT=256, pad_to, F)  # 绘制谱图
# plt.cohere(x, y, NFFT=256, Fs)  # 绘制X-Y相关性函数
# plt.scatter()  # 绘制散点图 x,y是相同长度的序列
# plt.step(x, y, where)  # 绘制步阶图
# plt.hist(x, bins, normed)  # 绘制直方图
# plt.contour(X, Y, Z, N)  # 绘制等值线
# plt.vlines()  # 绘制垂直线
# plt.stem(x, y, linefmt, markerfmt, basefmt)  # 绘制曲线每一个点到水平轴线的垂线
# plt.plot_date()  # 绘制数据日期
# plt.plotfile()  # 绘制数据后写入文件

# x = np.linspace(0, 8, 150)  # 从0到8分成150个点
# y = np.cos(2 * np.pi * x) * np.exp(-x) + 0.8  # 函数表示
# plt.plot(x, y, 'k', color='yellow', linewidth=6, linestyle='-')
# plt.show()

# plt库的坐标轴设置函数
# plt.axes('v','off','equal','scaled','tight','image')
# plt.xlim(xmin,xmax)
# plt.ylim(ymin,ymax)
# plt.xscale()
# plt.yscale()
# plt.autoscale()
# plt.text(x,y,s,fontdict,withdash)
# plt.thetagrids(angles,labels,fmt,frac)
# plt.grid(on/off)


# plt库的标签设置函数
# plt.figlegend(handles, label, loc)  # 为全局绘图区与放置图注
# plt.legend()  # 为当前坐标图放置图注
# plt.xlabel(s)  # 设置当前x轴的标签
# plt.ylabel(s)  # 设置当前y轴的标签
# plt.xticks(array, 'a', 'b', 'c')  # 设置当前x轴刻度位置的标签和值
# plt.yticks(array, 'a', 'b', 'c')  # 设置当前y轴刻度位置的标签和值
# plt.clabel(cs, v)  # 为等值线图设置标签
# plt.get_figlabels()  # 返回当前绘图区域的标签列表
# plt.figtext(x, y, s, fontdict)  # 为全局绘图区添加文字
# plt.title()  # 设置标题
# plt.suptitle()  # 为当前绘图区域设置中心标题
# plt.text(x, y, s, fontdict)  # 为坐标图轴添加注释
# plt.annotate(note, xy, xytext, xycoords, textcoords, arrowprops)  # 用箭头在指定数据点创建一个注释或者一段文本

# matplotlib.rcParams['font.family'] = 'SimHei'
# matplotlib.rcParams['font.sans-serif'] = ['SimHei']
# # plt.plot([1,0,1,0,1])
# plt.plot([1, 2, 4, 5], [1, 2, 3, 2.1], [1, 5, 6], [1, 8, 5])  # 先后两个数组分别代表了x轴和y轴
# plt.title("这里是标题")
# plt.xlabel("时间(s)")
# plt.ylabel("范围(m)")
# plt.xticks([1, 2, 3, 4, 5], [r'$\pi/3$', r'$2\pi/3$', r'$\pi$', r'$4\pi/3$'])
# plt.show()

# plt库的区域填充函数
# plt.fill(x, y, c, color)  # 填充多边形
# plt.fill_between(x, y1, y2, where, color)  # 填充两条曲线之间围成的多边形
# plt.fill_betweenx(y, x1, x2, where, hold)  # 填充两条水平线之间围成的区域

# 绘制一个带有局部 阴影的坐标系
x = np.linspace(0, 10, 100)  # 设置从0到10间断一百份
y = np.cos(2 * np.pi * x) * np.exp(-x) + 0.8  # 计算y的值
plt.plot(x, y, 'k', color='yellow', label="$exp_line$", linewidth=3)  # 绘制曲线
plt.axis([0, 6, 0, 1.9])  # 绘制子图 宽高从0到6 从0到1.9
ix = (x > 0.8) & (x < 3)  # 设置两端
plt.fill_between(x, y, 0, where=ix, facecolor='red', alpha=0.25)  # 在范围内填充颜色,透明度为25%
plt.text(0.5 * (0.8 + 3), 0.25, r"$\int_a^b f(x)\mathrm{d}x$", horizontalalignment="center")  # 编写阴影内部的函数
plt.legend()
plt.show()
