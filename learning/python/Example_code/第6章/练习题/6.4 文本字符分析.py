# -*- coding: utf-8 -*-
# @Time : 2020/7/6 14:29
# @Author : MYH
# @File : 6.4 文本字符分析.py
# @Software: PyCharm


# def getText():
#     text = open("Zen of Python.py", 'r').read()
#     text = text.lower()  # 进行字符小写化处理
#     for ch in ',-.#':  # 特殊字符的处理
#         text.replace(ch, ' ')
#     return text
#
#
# txt = getText()
# print(txt)
# # words = txt.split()  # 对文本进行分割
# # counts = {}  # 创建一个字典
# # for word in words:
# #     counts[word] = counts.get(word, 0) + 1
# # print(counts)
# # item = list(counts.items())  # 进行列表化存储
# # item.sort(key=lambda x: x[1], reverse=True)  # 逆序排列
# # for i in range(10):
# #     word, count = item[i]
# #     print("{0:<10}{0:>10}".format(word, count))

def getText():
    txt = open("../text/Zen of Python.py", "r").read()
    txt = txt.lower()  # 将全文进行单词小写处理
    for ch in '!"#$%^&*()_-=|~\\[]{}|`<>/?,.':  # 去除非英文单词中字符
        txt = txt.replace(ch, " ")
    return txt


words = []
text = getText()  # 获取文本
for ch in text:
    if ch not in [' ', '\n']:
        words += ch
# print(words)  # 测试输出
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1  # 向字典中添加数据
items = list(counts.items())  # 转换称列表
items.sort(key=lambda x: x[1], reverse=True)  # 逆向排序 进行排序
for i in range(10):
    word, count = items[i]
    print("{0:<3}的词频为: {1:>5}".format(word, count))

# 有兴趣可以尝试对中文文本进行字符分析
