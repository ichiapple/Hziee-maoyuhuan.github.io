# -*- coding: utf-8 -*-
# @Time : 2020/7/5 22:45
# @Author : MYH
# @File : 6.2 元素重复判定.py
# @Software: PyCharm

arr = ['柠檬','苹果', '香蕉', '橘子', '梨', '西瓜', '柠檬', '葡萄', '西瓜']
d = False
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] == arr[j]:
            d = True
            print("重复部分是{}".format(arr[i]))
            break

# print("end")
if d:
    print("列表中有重复")
else:
    print("列表中无重复")

