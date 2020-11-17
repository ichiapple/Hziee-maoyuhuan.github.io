# -*- coding: utf-8 -*-
# @Time : 2020/7/5 20:08
# @Author : MYH
# @File : 6.1 随机密码生成.py
# @Software: PyCharm

import random

s = ""  # 字符串
pwd = ""  # 密码串
for i in range(ord("A"), ord('Z') + 1):
    s += chr(i)
for i in range(ord('a'), ord('z') + 1):
    s += chr(i)
for i in range(ord('0'), ord('9') + 1):
    s += chr(i)
# print(s)#测试输出
# print(s[random.randint(0, len(s))])  # 测试输出
for i in range(8):
    ss = ""
    for i in range(10):
        ss += s[random.randint(0, len(s)-1)]
    print(ss)
