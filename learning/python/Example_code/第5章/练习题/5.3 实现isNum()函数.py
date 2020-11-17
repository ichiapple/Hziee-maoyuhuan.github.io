# -*- coding: utf-8 -*-
# @Time : 2020/7/4 14:53
# @Author : MYH
# @File : 5.3 实现isNum()函数.py
# @Software: PyCharm


# 参数为一个字符串 如果字符串属于整数/浮点数/复数则返回True 否则返回False
try:
    k = eval(input("请输入一个字符串进行判断: "))
    if isinstance(k,int):
        print("字符串是整数")
    elif isinstance(k,float):
        print("字符串是浮点数")
    elif isinstance(k,complex):
        print("字符串是复数")
    else:
        print("字符串是其他字符串")
except NameError:
    print("输入内容有误")


