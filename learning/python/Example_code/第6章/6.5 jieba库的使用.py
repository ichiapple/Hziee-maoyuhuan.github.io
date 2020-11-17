# -*- coding: utf-8 -*-
# @Time : 2020/7/5 12:57
# @Author : MYH
# @File : 6.5 jieba库的使用.py
# @Software: PyCharm

# 如果对于英文文本可以通过split方法进行分离提取单词 可是对于中文文本中缺少分隔符,所以有了"分词"问题 而jieba库则是python中一个重要的第三方中文分词函数库
# jieba库不是python自带库,所以需要我们自行安装 通过pip install jieba 命令完成安装 但是太慢了 需要使用国内的镜像源

# 引入jieba库
import jieba

# jieba.cut("你你你好")  # 精确模式 返回一个可迭代的数据类型
# jieba.cut(s, cut_all=True)  # 全模式 输出文本中所有可能的单词
# jieba.cut_for_search(s)  # 搜索引擎模式,蛇和搜索引擎建立索引的分词结束
# jieba.lcut(s)  # 建议使用 精确模式,返回一个列表类型
# jieba.lcut(s, cut_all=True)  # 建议使用 全模式 返回一个列表类型
# jieba.lcut_for_search(s)  # 搜索引擎模式 返回一个列表类型 建议使用
# jieba.add_word(w)  # 向分词词典中添加一个新词w
print(jieba.lcut("中国是我的祖国,中华人民共和国是一个伟大的国家"))  # 精确模式,输出的分词能够完整且不多于组成原始文本
print(jieba.lcut("中国是我的祖国,中华人民共和国是一个伟大的国家", cut_all=True))  # 返回安全模式,输出原始文本中可能产生的所有问题,冗余最大
print(jieba.lcut_for_search("中国是我的祖国,中华人民共和国是一个伟大的国家"))  # 搜索引擎模式,首先执行精确模式,然后再对其中的长词进行进一步切分

print(jieba.lcut("习大大在西湖游玩"))
jieba.add_word('习大大')  # 添加单词
print(jieba.lcut("习大大在西湖游玩"))
