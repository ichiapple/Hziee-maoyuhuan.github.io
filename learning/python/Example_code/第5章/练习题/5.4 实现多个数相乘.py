# -*- coding: utf-8 -*-
# @Time : 2020/7/4 15:02
# @Author : MYH
# @File : 5.4 实现多个数相乘.py
# @Software: PyCharm

def multi(*nums):
    res = 1
    for i in nums:
        res *= i
    return res


print(multi(1, 3, 4, 5))
