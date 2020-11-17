# -*- coding: utf-8 -*-
# @Time : 2020/7/3 20:55
# @Author : MYH
# @File : 4.2 统计不同字符的个数.py
# @Software: PyCharm

# 统计不同类型字符的个数 分英文大写/英文小写/数字/空白/其他字符
eng, ENG, num, space, oth = 0, 0, 0, 0, 0
str = input("请输入字符串.. ")
for i in str:
    if i.islower():
        eng += 1
    elif i.isupper():
        ENG += 1
    elif i.isnumeric():
        num += 1
    elif i.isspace():
        space += 1
    else:
        oth += 1

print("英文大写/英文小写/数字/空白/其他字符 的个数分别为: {},{},{},{},{}".format(eng,ENG,num,space,oth))