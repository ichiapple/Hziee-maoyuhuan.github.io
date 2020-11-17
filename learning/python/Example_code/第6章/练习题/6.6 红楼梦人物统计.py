# -*- coding: utf-8 -*-
# @Time : 2020/7/6 15:46
# @Author : MYH
# @File : 6.6 红楼梦人物统计.py
# @Software: PyCharm

import jieba


def getText():
    txt = open("../text/红楼梦.txt", "r", encoding='utf-8').read()
    return txt


exclude = ["什么",'一个',"我们","那里","如今","你们","说道",'知道',"这里","起来","姑娘","众人","他们"]
text = getText()
# print(text) #测试输出
words = jieba.lcut(text)
# print(words) # 测试输出
items = {}
for word in words:
    if len(word) not in range(2,4):
        continue
    else:
        items[word] = items.get(word, 0) + 1
for word in exclude:
    del (items[word])
ls = list(items.items())  # 转换为list集合
# print(ls)  # 测试输出
ls.sort(key=lambda x: x[1], reverse=True)
# print(ls)  # 测试输出
for i in range(15):
    word, count = ls[i]
    print("{0:<10} {1:>5}".format(word, count))  # 进行输出

# 不搞了,差不多就这个意思得了.
