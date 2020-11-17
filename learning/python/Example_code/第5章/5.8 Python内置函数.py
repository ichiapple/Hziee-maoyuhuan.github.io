# -*- coding: utf-8 -*-
# @Time : 2020/7/4 13:18
# @Author : MYH
# @File : 5.8 Python内置函数.py
# @Software: PyCharm

# python 内置了68个内置函数 不需要引用库而可以直接使用
# all() 函数一般针对组合类型的数据类型,如果其中每一个元素都是True则返回True否则为False 注意: 0,空串"",空列表[]都会被认为是False
# any() 函数和all函数相反,它只要有一个为True就返回True
# hash() 函数可以计算哈希的类型返回哈希值
# id() 函数返回对每一个数据的唯一编号 python将数据存储在内存中的地址作为其唯一编号
# reversed() 函数返回输入组合数据类型的逆序形式
# sorted() 函数对序列进行排序,默认升序排序
# type() 函数能返回数据对应的数据类型

ls = [5, 9, 1, 2, 3, 0]
print(all(ls))
print(any(ls))
str = "HelloWorld"
print(hash(str))
print(id(str))
print(reversed(ls))
print(ls)  # 查看当前的ls
print(sorted(ls, reverse=True))  # reversed属性能够逆序,也就是从默认的从小到大变化为从大到小
print(type(ls))
