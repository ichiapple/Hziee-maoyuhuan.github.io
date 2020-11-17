# -*- coding: utf-8 -*-
# @Time : 2020/7/4 13:39
# @Author : MYH
# @File : 5.1 输出一个更大的田字格.py
# @Software: PyCharm


def draw(level):
    for i in range(level):
        s = ''
        if i % 10 == 0:
            for j in range(level):
                if j % 10 == 0:
                    s += '+'
                else:
                    if j % 2 == 1:
                        s += ' '
                    else:
                        s += '-'
        else:
            if i % 2 == 0:
                for j in range(level):
                    if j % 10 == 0:
                        s += '|'
                    else:
                        s += ' '
            else:
                print("")
        print(s, end='')


try:
    a = eval(input("请输入数字:"))
    draw(a)
except NameError:
    print("输入错误,退出程序..")