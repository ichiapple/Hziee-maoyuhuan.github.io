# -*- coding: utf-8 -*-
# @Time : 2020/7/4 2:47
# @Author : MYH
# @File : 5.6 函数的递归.py
# @Software: PyCharm

import sys


# 递归的典型例子: 阶乘 数学归纳法
# 阶乘的特征: 存在一个或者多个基例,基例是确定的表达式,不需要继续递归 所有的递归必须以一个或者多个基例结尾
def fact(i):
    if i == 0:
        return 1
    else:
        return i * fact(i - 1)


num = eval(input("请输入一个整数/小数: "))
print(fact(abs(int(num))))  # 转换成了整数


# 字符串反转
def reverseStr(s):
    return reverseStr(s[1:]) + s[0]  # 这样写是要出问题的,因为没有个极限(停止的时候) python执行到1000次递归就会报错 most recent call last


sys.setrecursionlimit(2000)  # 设置新的递归层数 虽然这样写但是还是要出问题 因为递归本身就是没有穷尽的
# reverseStr('abc')


def newReverseStr(s):
    if s == '':
        return s
    else:
        return s[1:] + s[0]


print(newReverseStr(input("请输入一个字符串: ")))
