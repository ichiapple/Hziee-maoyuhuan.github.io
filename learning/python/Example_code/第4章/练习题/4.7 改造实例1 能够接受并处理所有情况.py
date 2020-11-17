# -*- coding: utf-8 -*-
# @Time : 2020/7/3 22:03
# @Author : MYH
# @File : 4.7 改造实例1 能够接受并处理所有情况.py
# @Software: PyCharm

# TempStr = input("请输入以C或者F结束符号的温度: ")
# if TempStr[-1] in ['F', 'f']:
#     C = (eval(TempStr[0: -1]) - 32) / 1.8
#     print("转换后的结果为: {:.2f}C".format(C))
# elif TempStr[-1] in ['C', 'c']:
#     F = (eval(TempStr[0: -1])) * 1.8 + 32
#     print("转换后的结果为: {:.2f}F".format(F))
# else:
#     print("输入格式错误.")

while True:
    tempNum = input("请输入一个C或者F结尾的温度值: ")
    try:
        s = tempNum[-1]
        tempNum = eval(tempNum[0:-1])
        if s in ['F', 'f']:
            C = (tempNum - 32) / 1.8
            print("转换后的结果为: {:.2f}C".format(C))
            break
        elif s in ['C', 'c']:
            F = tempNum * 1.8 + 32
            print("转换后的结果为: {:.2f}F".format(F))
            break
        else:
            print("输入格式错误,请重新输入")
            continue
    except NameError:
        print("请输入一个整数!")
        continue
