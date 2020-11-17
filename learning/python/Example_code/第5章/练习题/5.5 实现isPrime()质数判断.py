# -*- coding: utf-8 -*-
# @Time : 2020/7/4 15:04
# @Author : MYH
# @File : 5.5 实现isPrime()质数判断.py
# @Software: PyCharm

# 除了1和本身没有其他因子的数称为质数
def numIsPrime(num):
    res = False
    for i in range(2, num):
        if num % i == 0:
            break
        # print(i)
        res = True
    return res


def main():
    try:
        d = eval(input("请输入一个数: "))
        print("数字" + str(d) + "{}一个质数".format("是" if numIsPrime(d) else "不是"))
    except NameError:
        print("输入错误,即将退出程序")


main()
