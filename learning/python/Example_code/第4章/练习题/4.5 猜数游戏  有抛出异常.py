# -*- coding: utf-8 -*-
# @Time : 2020/7/3 21:45
# @Author : MYH
# @File : 4.5 猜数游戏  有抛出异常.py
# @Software: PyCharm

from random import *

s = randint(0, 10)
print(s)
num = 0
while True:
    try:
        k = eval(input("请输入你想猜的数字: "))
    except:
        print("输入错误,请输入一个数字!")
        continue
    num += 1
    if s == k:
        break
    elif s > k:
        print("你猜的太小了")
        continue
    elif s < k:
        print("你猜的太大了")
        continue
    else:
        print("请输入一个数字!")
        continue

print("恭喜你,猜中了! 你使用的次数为: {}".format(num))
