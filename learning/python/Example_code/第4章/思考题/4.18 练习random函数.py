# -*- coding: utf-8 -*-
# @Time : 2020/7/3 16:28
# @Author : MYH
# @File : 4.18 练习random函数.py
# @Software: PyCharm

# 导入库
from random import *

# 随机生成100以内的十个整数
for i in range(10):
    s = randint(0,100)
    print(s, end=' ')
else:
    print()

# 随机选取0到100之间的奇数
print(randrange(1, 100, 2))

# 随机选取"abcdefghjkl"中的4个字符
str = "abcdefghjkl"
print(sample(str, 4))

# 随机选择['apple','orange','green']中的一个字串
arr = ['apple','orange','green']
print(sample(arr, 1)[0])
