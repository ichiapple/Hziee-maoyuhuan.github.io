# -*- coding: utf-8 -*-
# @Time : 2020/7/9 4:58
# @Author : MYH
# @File : 7.4 一二维数据的格式化和处理.py
# @Software: PyCharm

# 一维数据由对等关系的有序或无序数据构成,采用线性方式组织,对应集合,数组等概念
# 二维数据由关联的数据关系组成,也称为表格数据,采用表格方式组织,对应矩阵等概念

# 数据包括文件存储和程序使用两个状态 存储不同维度的数据需要适合维度特点的文件存储格式 需要使用对应的数据类型或者结构 需要考虑存储格式和读写两个问题
# 一维数据使用分隔符(空格 逗号等形式)进行分割存储 使用逗号作为分隔符的格式称为CSV格式 是一种通用的,相对简单的数据存储格式具有下列规则
# 1. 纯文本格式,通过单一编码表示字符
# 2. 以行为单位,开头不允许留空行,行之间没有空行
# 3. 以行表示一个一维数据 多行表示二维数据
# 4. 以逗号(英文状态 半角)为分隔符进行分割每列数据,列数据为空也要保留逗号
# 5.对于表格数据,可以包含(或者不包含)列名,包含时列名放在第一行

# Python中提供了一个读写CSV的标准库 包含了操作CSV格式最基本的功能 csv.reader()和csv.writer()
# csv格式十分简单,建议自己编写csv操作函数 可以更加灵活和个性化 对于需要运行在复杂环境或者商业用途的程序建议使用csv标准库

# fo = open("file/price.csv", 'r',encoding='utf-8')  # 打开文件
# ls = []  # 创建一个空的集合
# for line in fo:  # 对文件逐行进行遍历
#     line = line.replace("\n", '')  # 将\n替换成空白
#     ls.append(line.split(","))  # 对行进行截断
# print(ls)  # 输出列表
# fo.close()  # 关闭文件


# 进行优化 还是有问题

# fo = open("file/price.csv", 'r', encoding='utf-8')  # 打开文件
# ls = []
# for line in fo:  # 对文件逐行进行遍历
#     line = line.replace("\n", '')  # 将\n替换成空白
#     # line = line.replace("[", '')  # 将\n替换成空白
#     # line = line.replace("]", '')  # 将\n替换成空白
#     ls = line.split(",")  # 对行进行截断
#     ins = ""
#     for s in ls:
#         ins += "{}\t".format(s)
#     print(ins)
#
# fo.close()  # 关闭文件

# 一维数据写入csv文件

# fo = open("file/price.csv", 'w', encoding='utf-8')  # 打开文件
# ls = ['南京', '100.0', '120.6', '121.3']
# fo.write(",".join(ls) + "\n")  # 基本写入格式
# fo.close()

# 二维数据的写入略