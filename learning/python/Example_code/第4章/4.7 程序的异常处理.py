# -*- coding: utf-8 -*-
# @Time : 2020/7/3 17:51
# @Author : MYH
# @File : 4.7 程序的异常处理.py
# @Software: PyCharm

# a = eval(input("请输入一个整数: "))
# print(a ** 2)

# 存在一定的问题,因为无法判断输入的内容是否为一个整数 所以需要用异常处理机制
try:
    a = eval(input("请输入一个整数: "))
    print(a ** 2)
except NameError:
    print("输入错误: 输入的非整数!")

# 错误和异常: 异常是程序执行过程中的问题,但是这个问题是可以预期到的,如果是预期不到的问题,那就是错误
# 其中也可以有高级用法包括使用else和finally
try:
    arr = "abcdefgh"
    index = eval(input("请输入一个7或以内的下标: "))
    s = arr[index]
    print(s)
except NameError:
    print("请输入一个整数")
except:  # 包含了下标越界的问题
    print("越界!")
else:
    print("try-catch正常,没有捕获异常")
finally:
    print("try-catch结束")

# 总体说来 try-catch尽量放在程序容易出错的地方进行包裹,如果滥用,则会降低代码可读性 不过为了用户体验,多用几个也未尝不可
