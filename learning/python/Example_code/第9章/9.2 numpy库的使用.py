# -*- coding: utf-8 -*-
# @Time : 2020/7/10 0:33
# @Author : MYH
# @File : 9.2 numpy库的使用.py
# @Software: PyCharm


# numpy库介绍: python标准库中提供了一个array类型 用于保存数组类型数据 但是不支持多维数据 处理函数不够丰富,不适合数值运算 故nubpy库得以发展
# 该库处理的最基础数据是由同种元素构成的多维数组 数组元素可以用整数索引(从0开始) 多维数组类型的维度叫做轴,轴个个数称为秩 一维秩为1 二维秩为2 ..

import numpy as np  # 引入numpy 给它起一个别名为np 其中as保留字和import合用,能够 改变后续代码中库的命名空间 有助于提高代码可读性

# numpy库函数解析
# np.array([x, y, z], dtype=int)  # 从python列表和元组中创建数组
# np.arange(x, y, i)  # 创建一个从x到y步长为i的数组
# np.linspace(x, y, n)  # 创建一个从x到y 等分成n个元素的数组
# np.indices((m, n))  # 创建一个m行n列的矩阵
# np.random.rand(m, n)  # 创建一个m行n列的随机数组
# np.ones((m, n), dtype)  # 创建一个m行n列全1数组 dtype是数据类型
# np.empty((m, n), dtype)  # 创建一个m行n列全0数组 dtype是数据类型

# ndarray的常用属性
# ndarray.ndim  # 数轴个数 秩
# ndarray.shape  # 数组在每个维度上大小的整数元组
# ndarray.size  # 数组元素的总个数
# ndarray.dtype  # 数组元素的数据类型 dtype类型可以用于创建数组
# ndarray.itemsize  # 数组中每一个元素的字节大小
# ndarray.data  # 包含实际数组元素的缓冲区地址
# ndarray.flat  # 数组元素的迭代器

a = np.ones((5, 5))
print(a)
print(a.ndim)
print(a.shape)
print(a.dtype)

# ndarray类的形态操作方法
# ndarray.reshape(m, n)  # 不改变数组ndarray 返回一个维度为(m,n)的数组
# ndarray.resize(new_shape)  # 直接修改数组array 和reshape一样
# ndarray.swapaxes(ax1, ax2)  # 将数组n个维度中任意两个维度进行调换
# ndarray.flatten()  # 对数据进行降维 返回一个折叠后的数组
# ndarray.ravel()  # 作用同flatten,返回的是数组的一个视图


# ndarray类的索引和切片方法
# x[i]  # 索引第i个元素
# x[-i]  # 从后向前数第i个元素
# x[n:m]  # 默认步长为1 从前往后 不含m
# x[-m:-n]  # 默认步长为1 从后往前 结束位置为n
# x[n:m:i]  # 指定步长为i的由n到m的索引

a = np.random.rand(6, 4)
print(a)
print(a[2])
print(a[1:3])
print(a[-4:-2])

# numpy库的算术运算符
# np.add(x1, x2[, y])  # y = x1 + x2
# np.subtract(x1, x2[, y])  # y = x1 - x2
# np.multiply(x1, x2[, y])  # y = x1 * x2
# np.divide(x1, x2[, y])  # y = x1 / x2
# np.floor_divide(x1, x2[, y])  # y = x1 // x2  返回值取整
# np.negative((x[, y]))  # y = -x
# np.power(x1, x2[, y])  # y = x1 ** x2
# np.remainder(x1, x2[, y])  # y = x1 % x2

# numpy库的比较运算符
# np.equal(x1, x2[, y])  # y = x1 == x2
# np.not_equal(x1, x2[, y])  # y = x1 != x2
# np.less(x1, x2[, y])  # y = x1 < x2
# np.less_equal(x1, x2[, y])  # y = x1 <= x2
# np.greater(x1, x2[, y])  # y = x1 > x2
# np.greater_equal(x1, x2[, y])  # y = x1 >= x2
# np.where(condition[x, y])  # 根据条件进行判断

print(np.less_equal([1, 2], [2, 2]))

# numpy库的其他运算函数
# np.abs(x)  # 计算绝对值
# np.sqrt(x)  # 计算每一个元素的平方根
# np.square(x)  # 计算每一个元素的平方
# np.sign(x)  # 计算每一个元素的符号 正为1 0为0 负为-1
# np.ceil(x)  # 计算大于等于每一个元素的最小值
# np.floor(x)  # 计算小于等于每一个元素的最大值
# np.rint(x[, out])  # 圆整,取每一个元素最近的整数,保留数据类型
# np.exp(x[, out])  # 计算每一个元素的指数值
# np.log(x), np.log10(x), np.log2(x)  # 计算自然对数

print(np.abs([-1.3, 2]))
print(np.ceil([-1.3, 2]))
