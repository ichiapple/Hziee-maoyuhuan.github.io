# -*- coding: utf-8 -*-
# @Time : 2020/7/6 14:23
# @Author : MYH
# @File : 6.3 元素重复判定 续.py
# @Software: PyCharm

arr = ['柠檬', '苹果', '香蕉', '橘子', '梨', '西瓜', '柠檬', '葡萄', '西瓜']
# arr1 = ['柠檬', '苹果', '香蕉', '橘子', '梨', '西瓜', '葡萄']
d = False
if len(arr) != len(set(arr)):  # 使用集合的无重复性进行判断
    d = True

if d:
    print("列表中有重复")
else:
    print("列表中无重复")
