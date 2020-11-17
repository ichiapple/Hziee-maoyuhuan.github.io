# -*- coding: utf-8 -*-
# @Time : 2020/7/4 14:45
# @Author : MYH
# @File : 5.2 实现isOdd()函数.py
# @Software: PyCharm

def isOddNum(num):
    if num % 2 == 0:
        print("偶数")
    else:
        print("奇数")


while True:
    try:
        k = eval(input("请输入一个数字"))
        isOddNum(k)
        break
    except NameError:
        print("请输入一个数字! 请重新输入:")
        continue
