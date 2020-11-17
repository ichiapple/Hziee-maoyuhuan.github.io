# -*- coding: utf-8 -*-
# @Time : 2020/7/3 22:46
# @Author : MYH
# @File : 5.1 函数的基本使用.py
# @Software: PyCharm

# python中函数的定义一定要放在调用前面
def happy():
    print("Happy birthday to you!")


def happyName(name):
    print("Happy birthday to {}!".format(name))


def happySong(name1, name2):
    happy()
    happy()
    happyName(name1)
    happy()
    print()
    happy()
    happy()
    happyName(name2)
    happy()


happySong('Jack', 'Lisy')

f = lambda x, y: x + y  # lambda保留字定义了一种特殊的函数--匿名函数 又称为lambda函数 格式为 <函数名> = lambda <参数列表>: <表达式>
print(type(f))  # 说明这是一个函数
print(f(23, 56))  # 可进行函数一样的操作
