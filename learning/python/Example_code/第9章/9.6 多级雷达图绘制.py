# -*- coding: utf-8 -*-
# @Time : 2020/7/11 18:59
# @Author : MYH
# @File : 9.6 多级雷达图绘制.py
# @Software: PyCharm

# 雷达图是通过多个离散属性比较对象的直观工具 本实例通过python绘制多级雷达图

# 导入部分
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# 设置字体
matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.sans-serif'] = ['SimHei']

# labels = np.array(['综合', 'KDA', '发育', '推进', '生存', '输出'])  # 设置属性
# nattr = 6  # 设置边数
# data = np.array([7, 6, 5, 4, 3, 6])  # 设置数值
# angles = np.linspace(0, 2 * np.pi, nattr, endpoint=False)  # 设置列表从0开始到2pi,间隔6个,设置为无末点
# data = np.concatenate((data, [data[0]]))
# angles = np.concatenate((angles, [angles[0]]))
# fig = plt.figure(facecolor="white")  # 设置一个全局绘图区域 背景颜色为白色
# plt.subplot(111, polar=True)  # 绘制一个子图 polar属性表示绘制的是一个极坐标
# plt.plot(angles, data, 'bo--', color='green', linewidth=2)  # 绘制曲线 --表示虚线 -表示实线 o表示小圆点
# plt.fill(angles, data, facecolor='yellow', alpha=0.3)  # 填充颜色 透明度为0.3
# plt.thetagrids(angles * 180 / np.pi, labels)  # 将对应的角度设置为对应的标题
# plt.figtext(0.15, 0.9, 'Dota能力值雷达图', ha='center')    #设置标题的位置以及文字 向右,向上数值增大
# plt.grid(True)#内部线条
# plt.savefig("file/Dota.png")  # 保存为图片
# plt.show()  # 进行展示

radar_labels = np.array(['研究型', '艺术型', '社会型', '企业型', '常规型', '现实型'])  # 设置类别
nattr = 6
data = np.array([
    [0.4, 0.32, 0.85, 0.33, 0.6, 0.84],
    [0.2, 0.2, 0.25, 0.3, 0.4, 0.64],
    [0.3, 0.12, 0.45, 0.7, 0.2, 0.24],
    [0.6, 0.7, 0.15, 0.9, 0.23, 0.14],
    [0.7, 0.42, 0.45, 0.1, 0.4, 0.74],
    [0.09, 0.92, 0.8, 0.3, 0.7, 0.44]
])  # 数据设置
data_labels = ('A成员', 'B成员', 'C成员', 'D成员', 'E成员', 'F成员')  # 数据标签
angles = np.linspace(0, 2 * np.pi, nattr, endpoint=False)  # 设置列表从0开始到2pi,间隔6个,设置为无末点
data = np.concatenate((data, [data[0]]))
angles = np.concatenate((angles, [angles[0]]))
fig = plt.figure(facecolor='white')
plt.subplot(111, polar=True)  # 绘制子图
plt.plot(angles, data, 'bo-', color='gray', linewidth=1, alpha=0.2)  # 画带点实线 灰色底线
plt.plot(angles, data, 'o--', linewidth=1, alpha=0.2)  # 画彩色线条
plt.fill(angles, data, alpha=0.25)  # 填充
plt.thetagrids(angles * 180 / np.pi, radar_labels)  # , frac=1.2属性会报错
plt.figtext(0.52, 0.95, "霍兰德人格分析", ha='center', size=20)
legend = plt.legend(data_labels, loc=(0.94, 0.8), labelspacing=0.2)  # 图注位置
plt.setp(legend.get_texts(), fontsize='small')
plt.grid(True)
plt.savefig("file/huolanderenge.png")
plt.show()
