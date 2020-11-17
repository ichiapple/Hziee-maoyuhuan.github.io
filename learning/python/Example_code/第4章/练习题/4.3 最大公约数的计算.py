# -*- coding: utf-8 -*-
# @Time : 2020/7/3 21:14
# @Author : MYH
# @File : 4.3 最大公约数的计算.py
# @Software: PyCharm

# 得到最大公约数和最小公倍数

M, N = eval(input("请输入两个整数.. "))
Multi= M*N
Rem = 0
while(N > 0):
    Rem = M % N
    M = N
    N = Rem

print("最大公因数为: {}".format(M))
R = Multi/M
print("最小公倍数为: {:.0f}".format(R))
