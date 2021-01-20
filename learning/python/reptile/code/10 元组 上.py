# -*- coding: utf-8 -*-
# @Time : 2021/1/19 14:37
# @Author : MYH
# @File : 10 元组 上.py
# @Software: PyCharm

tup1 = ()  # 创建一个空元组
print(type(tup1))  # 判断是一个 元组

tup2 = (40)  # 想创建一个单一元素的元组
print(type(tup2))  # 判断结果是 int

tup3 = (40,)  # 想创建一个单一元素的元组
print(type(tup3))  # 判断结果是一个 元组 表示元组只有单一元素的时候后面需要添加逗号

tup4 = (2020, 2021, "hello", "world")
print(tup4[3])  # 可以像数组那样访问
