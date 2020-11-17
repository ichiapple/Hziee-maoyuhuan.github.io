# -*- coding: utf-8 -*-
# @Time : 2020/7/11 1:50
# @Author : MYH
# @File : 9.5 科学坐标图绘制.py
# @Software: PyCharm

# 科学坐标图包含内容: 坐标轴 数据曲线 标题 图注
# 使用不同颜色不同形式两条曲线进行演示

# 导入部分
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# 设置字体
matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.sans-serif'] = ['SimHei']


# 绘制函数
def Draw(pcolor, nt_point, nt_text, nt_size):
    plt.plot(x, y, 'k', label='$exp_decay$', color=pcolor, linewidth=3, linestyle="-")  # x与y绘制曲线
    plt.plot(x, z, "b--", label='$cos(x^2)$', linewidth=2)  # x与z绘制曲线
    plt.xlabel("时间(t)")  # 设置x轴标题
    plt.ylabel("幅度(mV)")  # 设置y轴标题
    plt.title("阻尼衰减曲线绘制")  # 设置标题
    plt.annotate('$\cos(2\pi t) \exp(-t)$', xy=nt_point, xytext=nt_text, fontsize=nt_size,
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.1'))  # 指向曲线的提示 添加动态提示


def shadow(a, b):  # 绘制阴影
    ix = (x > a) & (x < b)
    plt.fill_between(x, y, 0, where=ix, facecolor='grey', alpha=0.4)
    plt.text(0.5 * (a + b), 0.2, r"$\int_a^b f(x)\mathrm{d}x$", horizontalalignment="center")


def XY_Axis(xstart, xend, ystart, yend):  # 设置边界
    plt.xlim(xstart, xend)
    plt.ylim(ystart, yend)
    plt.xticks([np.pi / 3, 2 * np.pi / 3, np.pi, 4 * np.pi / 3, 5 * np.pi / 3],
               ['$\pi/3$', "$2\pi/3$", '$\pi$', '$4\pi/3', '5\pi/3'])


x = np.linspace(0, 6, 100)  # 创建一个从0到6等分成100份的图
y = np.cos(2 * np.pi * x) * np.exp(-x) + 0.8  # 设置第一条曲线的函数
z = 0.5 * np.cos(x ** 2) + 0.8  # 设置第二条曲线的函数
note_point, note_text, notesize = (1, np.cos(2 * np.pi) * np.exp(-1) + 0.8), (1, 1.4), 14
fig = plt.figure(figsize=(8, 6), facecolor='white')  # 这里的fig好像并没有什么用
plt.subplot(111)  # 创建一个1*1的空白区域并在1号区域进行绘制
Draw("red", note_point, note_text, notesize)  # 绘制曲线
XY_Axis(0, 5, 0, 1.8)  # 设置边界 横轴从0到5 纵轴从0到1.8
shadow(0.8, 3)  # 绘制阴影
plt.legend()  # 放置图注
plt.savefig("file/sample.jpg")  # 存储为图像
plt.show()  # 展示图片

# 科学计算与可视化
# 可视化技术与科学计算相结合形成可视化技术的一个重要分支,科学计算可视化 可以将获得的数据以直观的图形图像方式展示
