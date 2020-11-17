# -*- coding: utf-8 -*-
# @Time : 2020/7/9 5:35
# @Author : MYH
# @File : 7.7 JSON库的使用.py
# @Software: PyCharm

# 导入: 使用import json命令进行导入json库
# json库包含了两个过程: 编码和解码 编码将python数据类型转换为json格式 解码是从json数据格式中解析数据到python数据类型 相互是序列化和反序列化的过程

# 其中json库有4个操作:
# json.dumps(obj, sort_key=False, indent=None)  # 将python的数据类型转换为json格式 编码过程 obj可以是python的列表或字典类型 默认生成的字符串按照顺序存放 indent参数用于控制缩进
# json.loads(string)  # 将json格式字符串转换为python的数据类型 解码过程
# json.dump(obj, fp, sort_key=False, indent=None)  # 功能与dumps()一致,输出到文件fp
# json.load(fp)  # 功能与load()一致,从文件fp进行读入

from json import *

dt = {'b': 2, 'a': 1, 'd': 4, 'c': 3}
s1 = dumps(dt)  # 返回json格式的字符串类型
s2 = dumps(dt, sort_keys=True, indent=4)  # 有缩进 按照key进行排序
print(s1)
print(s2)
print(s1 == s2)  # 两个不是同一个json数据
dt2 = loads(s2)
print(dt2,type(dt2))
