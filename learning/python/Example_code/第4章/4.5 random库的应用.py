# -*- coding: utf-8 -*-
# @Time : 2020/7/3 15:26
# @Author : MYH
# @File : 4.5 random库的应用.py
# @Software: PyCharm

# random库才哦那个梅森寻转算法生成伪随机数序列 因为做不到真正的随机 其结果其实是可以预期的
import random  # 当然也可以写成from random import *

print(random.seed())  # 初始化随机数种子,默认为当前系统时间 参数a=None
print(random.random())  # 生成一个[0.0,1.0)的随机小数
print(random.randint(5, 16))  # 生成一个[a,b]中的一个整数
print(random.getrandbits(10))  # 生成一个k比特长度的随机数
print(random.randrange(1, 99, 10))  # 生成一个[start,stop)之间的步进为step的随机整数(步进可以省略)
print(random.uniform(3.2, 6.3))  # 得到一个[start,stop]中的随机小数
print(random.choice("RIT"))  # 得到序列中的其中一个选项
print(random.choices("RIT"))  # 比较复杂 具体百度..
ls = list(range(10))
print(ls)
random.shuffle(ls)  # 将序列顺序打乱输出 不能直接在print函数中写shuffle
print(ls)
date = [random.randint(10, 20) for _ in range(10)]  # 设定范围
c = random.sample(date, 5)  # 从范围中选取5个数字
print(c)

# seed种子通过seed()函数指定随机数种子,随机数种子一般是一个整数,如果种子一样,则每次产生的随机序列也一样
random.seed(125)
print("{},{},{}".format(random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)))
print("{},{},{}".format(random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)))
random.seed(125)  # 重新设定seed的值,能够重新进行这个种子产生随机数序列
print("{},{},{}".format(random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)))
print("{},{},{}".format(random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)))
# 能够看出,在设定相同的种子后,每次调用随机函数生成的随机数是相同的 这也是随机数种子的作用 也是其应用之一
