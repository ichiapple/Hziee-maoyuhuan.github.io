# -*- coding: utf-8 -*-
# @Time : 2020/7/5 14:48
# @Author : MYH
# @File : 6.6 文本词频统计.py
# @Software: PyCharm


# 哈姆雷特词频统计
# 哈姆雷特的全文可以通过网上找到
# 统计第一步是分解并去除英文文章中的单词 因为单词可能会有大小写的形式 所以将全部都化为小写 排除大小写影响
# 同时需要对分隔符进行统一 因为原文可能有很多种标点符号 可以使用replace方法进行替换
# 同时需要对分隔符进行统一 因为原文可能有很多种标点符号 可以使用replace方法进行替换成空格再进行统计
# 第二步就是对每一个单机进行奇数 同时需要考虑到加入新词的问题
# if word in counts:
#     counts[word] += 1
# else:
#     counts[word] = 1
# 当然可以简化写成 count是[word] = counts.get(word,0)+1
# 第三步就是对单词的统计结果按照频率从高到低进行排序,选取十个进行打印输出 使用sort()方法和lambda函数配合实现排序

# def getText():
#     txt = open("text/Hamlet.txt", "r").read()
#     txt = txt.lower()  # 将全文进行单词小写处理
#     for ch in '!"#$%^&*()_-=|~\\[]{}|`<>/?,.':  # 去除非英文单词中字符
#         txt = txt.replace(ch, " ")
#     return txt
#
#
# hamletText = getText()  # 获取文本
# words = hamletText.split()  # 进行分离
# counts = {} #创建一个字典
# for word in words:
#     counts[word] = counts.get(word, 0) + 1  #向字典中添加数据
# items = list(counts.items())  # 转换称列表
# items.sort(key=lambda x: x[1], reverse=True)  # 逆向排序 进行排序
# for i in range(10):
#     word, count = items[i]
#     print("{0:<10} {1:>5}".format(word, count))


# 因为达索是冠词/代词/连接词 并不能代表文章的含义 所以稍微优化了一点
# excludes = {'the', 'and', 'of', 'you', 'i', 'my', 'in'}  # 排除数组
#
#
# def getText():
#     txt = open("text/Hamlet.txt", "r").read()
#     txt = txt.lower()  # 将全文进行单词小写处理
#     for ch in '!"#$%^&*()_-=|~\\[]{}|`<>/?,.':  # 去除非英文单词中字符
#         txt = txt.replace(ch, " ")
#     return txt
#
#
# hamletText = getText()  # 获取文本
# words = hamletText.split()  # 进行分离
# counts = {}  # 创建一个字典
# for word in words:
#     counts[word] = counts.get(word, 0) + 1  # 向字典中添加数据
# for word in excludes:
#     del (counts[word])  # 如果单词是再排除列表中的则进行删除
# items = list(counts.items())  # 转换称列表
# items.sort(key=lambda x: x[1], reverse=True)  # 逆向排序 进行排序
# for i in range(10):
#     word, count = items[i]
#     print("{0:<10} {1:>5}".format(word, count))


# 三国演义词频统计 因为是中文统计词频所以需要用到结巴库
# import jieba
#
# txt = open("text/三国演义.txt", "r", encoding='gb18030').read()
# words = jieba.lcut(txt)  # 进行切割 提取单词
# # print(txt) # 测试输出
# counts = {}  # 用于统计单词出现次数
# for word in words:
#     if len(word) == 1:
#         continue  # 如果只是单个字的词就跳过
#     else:
#         counts[word] = counts.get(word, 0) + 1
# item = list(counts.items())  # 每一项进行提取形成一个列表
# item.sort(key=lambda x: x[1], reverse=True)  # 进行逆序排序
# for i in range(15):
#     word, count = item[i]
#     print("{0:<10} {1:>5}".format(word, count))  # 进行输出

# 看起来曹操是出现频率最高的,但是刘玄德就是刘备,所以我们要做一个进一步处理
# 首先像前面那样进行excludes的排除 然后对相同意义的词进行合并
import jieba

excludes = {"将军", "却说", "荆州", "二人", "不可", "不能", "如何", "如此", "商议", "军士", "大喜", "次日", '左右', "军马", "天下", "于是", "今日","引兵"}
txt = open("text/三国演义.txt", "r", encoding='gb18030').read()
words = jieba.lcut(txt)  # 进行切割 提取单词
# print(txt) # 测试输出
counts = {}  # 用于统计单词出现次数
for word in words:
    if len(word) == 1:
        continue  # 如果只是单个字的词就跳过
    elif word == "诸葛亮" or word == "孔明曰" or word == "诸葛孔明":
        word = "孔明"
    elif word == "关公" or word == "云长" or word == "关云长":
        word = "关羽"
    elif word == "玄德" or word == "刘玄德" or word == "玄德曰" or word == "主公":
        word = "刘备"
    elif word == "蒙德" or word == "丞相":
        word = "曹操"
    else:
        counts[word] = counts.get(word, 0) + 1
for word in excludes:
    del (counts[word])  # 如果单词是再排除列表中的则进行删除
item = list(counts.items())  # 每一项进行提取形成一个列表
item.sort(key=lambda x: x[1], reverse=True)  # 进行逆序排序
for i in range(15):
    word, count = item[i]
    print("{0:<10} {1:>5}".format(word, count))  # 进行输出
