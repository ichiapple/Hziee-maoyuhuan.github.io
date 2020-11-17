# -*- coding: utf-8 -*-
# @Time : 2020/7/6 16:13
# @Author : MYH
# @File : 7.1 文件的使用.py
# @Software: PyCharm

# 文件概念: 文件时一个存储在辅助存储器上的数据序列,可以包含任何数据内容 文件是数据的集合和抽象 用文件形式组织和表达数据更加有效且灵活
# 包含了两种类型: 文本文件和二进制文件
# 文本文件由单一的字符编码的字符组成 内容容易统一展示和阅读 例如txt文件
# 二进制文件直接由二进制位0或者1组成 没有统一编码 文件内部的数据与文件用途有关 按照特定格式形成文件 由于没有统一编码,所以只能当作字节流不能看作为字符串
# open(<打开文件的路径>,<打开模式>)

textFile = open("file/output.txt", 'rt', encoding='utf-8')  # 这里的rt表示只读且以文本文件的形式进行打开 需要指定字符编码
print(textFile.readline())
textFile.close()  # 进行关闭
binFile = open("file/output.txt", 'rb')  # 只读且以二进制文件形式进行打开
print(binFile.readline())  # 因为采用二进制方式打开文件，文件会被解析为字节流，字符串中的一个字符使用两个字节表示
binFile.close()

# 打开模式说明: 打开模式共有7种
# 'r'只读 'w'覆盖写(不存在则创建,存在则覆盖原文件) 'x'创建写(创建新文件,如果存在则报错) 'a'追加写(不存在则创建,如果存在则追加)
# 'b'二进制文件格式 't'默认值,文本文件格式 '+'与r/x/w/a一同使用,在原功能基础上增加同时读写功能

# 同时能够对二进制文件进行打开
# a = open("file/bmp.bmp",'rb')
# print(a.readline())
# a.close()

# 当文件被打开后,根据打开方式的不同,可以对文件进行相应的读写操作 读写文本文件则按照当前计算机编码的字符串方式打开 读写二进制文件的时候按照字节流打开
# Python提供了4种内容读取方法 <file>.readall() <file>.read(size=-1) <file>.readline(size=-1) <file>.readlines(hint=-1) 字符串或者字节流取决于文件打开格式
# fname = input("请输入要打开的文件:")
# file = open(fname, 'r', encoding='utf-8')
# for line in file.readlines():  # 当然也可以直接写成for line in file: 建议使用后面这种形式
#     print(line)
# file.close()

# 内容写入方法
# <file>.write(s) 向文件写入一个字符串或者字节流
# <file>.writelines(lines)将一个元素全为字符串的列表写入文件
# <file>.seek(offset) 改变当前文件指针的位置(0-文件开头 1-当前位置 2-文件末尾)
filename = input("请输入要写入的文件名:")
fo = open(filename, "w+")
ls = ['唐诗', '宋词', '元曲']
fo.writelines(ls)  # 并不是添加一行的意思,这只是排列输出的意思
fo.seek(0)  # 让指针移动到文件头部,这样我们进行遍历的时候可以读取到文本
for lines in fo:
    print(lines)
fo.close()
