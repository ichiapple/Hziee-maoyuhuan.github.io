# -*- coding: utf-8 -*-
# @Time : 2020/7/4 18:13
# @Author : MYH
# @File : 6.1 组合数据类型概述.py
# @Software: PyCharm

# 计算机步进要对单个变量进行处理 同时也需要对一组数据进行批量处理
# 组合数据类型可以分为三类:
# 序列类型 (元素向量,元素之间存在先后关系 通过序号访问 元素之间不排他) 字符串 元组 列表
# 集合类型 (元素集合 元素之间无序 相同元素在集合中唯一存在) 集合
# 映射类型 (键值对数据项的组合 每一个元素是一个Key-Value对 表示为: (key, value)) 字典

# 序列类型常用的操作符:
# x in s      如果x是s元素 则返回True
# x not in s  如果x不是s元素 则返回True
# s + t       连接S和T
# s * n / n * s   将序列s复制n次
# s[i]        获取序列s下标为i的元素 索引
# s[i:j]      获取序列s下标从i开始到j(不包含j)的子序列 切片
# s[i:j:k]    获取序列s下标从i开始到j(不包含j)的子序列 其步长为k 步骤分片
# len(s)      获取序列的长度
# min(s)      获取序列s中最小元素
# max(s)      获取序列s中最大元素
# s.index(x[,i[,j]])      序列s中从i开始到j位置第一次出现x元素的位置
# s.count(x)  序列s中x出现的总次数

# 元组(tuple) 是序列类型中比较特殊的一种,一旦被创建则不能进行修改
tu = "cat", 'dog', 0x8822, "12"
print(tu)
color = "red", 'green', tu
print(color)
print(color[1])
print(color[-1][2])  # 获取的是color的最后一个元素中的下标为2的元素


def func(x):
    return x, x ** 3  # 可以多值返回


print(func(3))

a, b = "dog", 'cat'
b, a = a, b  # 这个写法在python中是可以的 用于交换a和b
print(a, b)

import math

for x, y in ((1, 0), (2, 8), (3, 4)):
    print(math.hypot(x, y), end='  ')  # 求坐标到原点的距离

# 集合类型 包含了0个或多个数据项的无序集合 集合元素不可以重复 能够进行hash运算的类型都可以作为集合的元素
# 这些哈希值和内容是无关的 也和组合无关,哈希是数据在另一个维度的体现
print(hash("Python"))
print(hash("Is"))
print(hash("Good"))
print(hash("PythonIsGood"))

S = {12, 45, "323"}
print(S)
T = {12, 12, 12, (12, 45), "323"}  # 多个相同元素会被看作一个元素并且没有先后索引和位置关系 所以不能分片
print(T)

# set函数可以生成一个集合 参数可以是任何组合的数据类型 返回是一个无序无重复的任意集合
V = set("Apple")
print(V)
B = {"apple", "bag", 'human'}
print(B)

# 集合类型的操作符:
# S-T 或者 S.difference(T)              返回一个新的集合 包括在S中但是不是在T中的元素
# S-=T 或者 S.difference_update(T)      更新集合S 减去S交T
# S&T 或者 S.intersection(T)            返回一个S和T的交集
# S&=T 或者 S.intersection_update(T)    更新集合S为S和T的交集
# S^T 或者 S.symmetric_difference(T)            返回一个集合,是S和T中的元素但不包含都在的部分
# S^=T 或者 S.symmetric_difference_update(T)    更新集合S为S和T中的元素但不包含都在的部分
# S|T 或者 S.union(T)                   返回一个集合 包括在S和T中的元素
# S|=T 或者 S.update(T)                 更新集合S为S和T中的元素
# S<=T 或者 S.issubset(T)               如果S为T的子集则返回True 如果操作为<则是真子集
# S>=T 或者 S.issuperset(T)             如果S为T的超集则返回True 如果操作为>则是真超集
# 可以使用韦恩图进行图像的说明

# 集合类型有10种操作函数/方法
# S.add(x)            如果数据x不在S中则将x添加到S中
# S.clear()           移除S中的所有数据项
# S.copy()            返回集合S的一个副本
# S.pop()             返回集合S中的一个元素,如果S为空则产生一个异常KeyError
# S.discard(x)        如果x在集合S中,则移除该项,如果不存在这样的x则不报错
# S.remove(x)         如果x在集合S中,则移除该项,如果不存在则产生一个异常KeyError
# S.isdisjoint(T)     如果S和T中没有相同的元素则返回True
# len(S)              返回集合的长度
# x in S              如果x是S的元素则返回True 否则返回False
# x not in S          如果x不是S的元素则返回True 否则返回False

# 集合类型主要用于三个场景: 成员关系测试 / 元素去重复 / 删除数据项

print("Python" in ["Python", "big", "pen"])  # 成员关系测试
tu = (123, 456, 'adjkl', 'adjkl', 123)
print(set(tu))  # 去重复功能
newTu = tuple(set(tu) - {456})  # 因为是集合之间的操作,所以后面的'456'需要加上花括号
print(newTu)

# 映射类型 主要以字典的形式进行体现
# 映射类型是键值对的形式存在的,每一个元素都是一个键值对,元素之间是无序的,是一种二元关系,key表示一个属性,或者类别或者项目,value就是属性的内容
