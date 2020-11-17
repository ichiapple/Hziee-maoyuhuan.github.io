# -*- coding: utf-8 -*-
# @Time : 2020/7/9 20:38
# @Author : MYH
# @File : 8.7 pip安装脚本.py
# @Software: PyCharm

# pip工具安装第三方库的格式为: pip install <库名称> 这里列举一些第三方python库
# numpy, 矩阵运算
# matplotlib, 产品级2D图形绘制
# PIL(pillow), 图像处理
# sklearn, 机器学习和数据挖掘
# requests, Http协议访问
# jieba, 中文分词
# beautiful_soup / bs4, html和xml文件解析
# wheel, python文件打包
# pyinstaller, 打包python源文件成可执行文件
# django, python最流行的web开发框架
# flask, 轻量级web开发框架
# werobot, 微信机器人开发框架
# networkx, 复杂网络和图结构的建模分析
# sympy, 数字符号计算
# pandas, 高效数据分析
# pyqt5, 基于Qt的专业GUI开发框架
# pyopengl, 多平台OpenGL开发接口
# pypdf2, pdf文件内容提取及处理
# docopt, python命令行解析
# pygame, 简单小游戏开发开发框架

# 自动安装脚本

import os

libName = {'numpy', 'matplotlib', 'pillow', 'sklearn', 'requests', 'jieba', 'beautifulsoup4', 'wheel', 'pyinstaller',
           'django', 'flask', 'werobot', 'networkx', 'sympy', 'pandas', 'pyqt5', 'pyopengl', 'pypdf2', 'docopt',
           'pygame'}

# 时间过长暂不展示
try:
    for lib in libName:
        os.system("pip install " + lib)
    print("succeed")
except:
    print("Fail!")
