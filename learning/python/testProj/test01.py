# -*- coding: utf-8 -*-
# @Time : 2020/11/18 11:25
# @Author : MYH
# @File : test01.py
# @Software: PyCharm

# print ("Hello world")

fp = open('C:/text.txt', 'a+')
print('hello world',file =fp)
fp.close()