# -*- coding: utf-8 -*-
# @Time : 2020/7/4 22:52
# @Author : MYH
# @File : 6.3 基本统计值运算.py
# @Software: PyCharm


# 调用了一系列的函数/方法 实现了对应的功能,增强代码可读性
from math import sqrt


def getNum():  # 获取用户输入
    nums = []
    num = input("请输入一个数字,按回车直接退出.  --->  ")
    while num != '':
        nums.append(eval(num))  # 追加到列表后
        num = input("请输入一个数字,按回车直接退出.  --->  ")
    return nums  # 返回数字列表


def mean(numbers):  # 计算平均值
    s = 0.0
    for number in numbers:
        s += number
    return s / len(numbers)


def dev(numbers, mean):  # 计算标准差
    sdev = 0.0
    for number in numbers:
        sdev += (number - mean) ** 2
    return sqrt(sdev / (len(numbers) - 1))


def median(numbers):  # 计算中位数
    newArr = sorted(numbers)  # 进行排序
    print(newArr)
    size = len(numbers)  # 长度
    if size % 2 == 0:
        midNum = (newArr[size // 2 - 1] + newArr[size // 2]) / 2
    else:
        midNum = (newArr[size // 2])
    return midNum


def main():
    n = getNum()
    m = mean(n)
    print("平均值:{},标准差:{:.3f},中位数:{}".format(m, dev(n, m), median(n)))


main()
