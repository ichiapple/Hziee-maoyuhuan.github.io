# -*- coding: utf-8 -*-
# @Time : 2020/7/6 15:23
# @Author : MYH
# @File : 6.5 生日悖论.py
# @Software: PyCharm

# 如果房间中有23人或者以上,则至少有2人相同生日的概率大于0.5 输出在不同的随机样本数量下,23人至少两人生日相同的概率
import random


def func(lst):  # 定义函数，判断列表中是否有重复元素
    lst1 = set(lst)
    if len(lst) > len(lst1):
        return True
    else:
        return False


tr = 10000
count = 0
for num in range(tr):  # 模拟10000次随机试验
    birthday = []  # 生成一个数组
    for i in range(23):  # 生成【1，365】之间的23个随机整数
        a = random.randint(1, 365)  # 生成一个1-365之间的随机数
        birthday.append(a)
        if func(birthday):  # 如果列表中有重复元素，则为True
            count = count + 1
print("{}%".format(count / tr))# 百分比输出
