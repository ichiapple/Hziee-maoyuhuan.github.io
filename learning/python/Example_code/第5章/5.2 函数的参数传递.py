# -*- coding: utf-8 -*-
# @Time : 2020/7/3 22:58
# @Author : MYH
# @File : 5.2 函数的参数传递.py
# @Software: PyCharm


# 函数的默认值
def multipleNum(num1=2, num2=4):  # 默认值必须从后往前默认
    return num1 * num2


print(multipleNum())  # 会使用默认的值
print(multipleNum(3, 5))  # 会使用两个新传入的值
print(multipleNum(9))  # 将a替换为新传入的值 b不变


# 通过在参数前面加* 表示可变数量的参数 只能加在参数列表的末尾,这些元素作为元组类型进行传入
def vfunc(a, *b):
    print(type(b))
    for i in b:
        a += i
    return a


print(vfunc(1, 2, 3, 4))  # tuple是元组/数组的意思 目前可以认为是一组元素


# 当然,形参名如果很多一一对应会很麻烦 python为了解决这个问题可以使用 变量=值 的方式进行函数的赋值
def add(a=1, b=2, c=3, d=4):
    return a + b + c + d


add(c=7, a=4)  # 如果用这个方式进行函数调用的时候 函数赋值的顺序可以打乱


# 函数可以没有返回值(例如之前的打印生日快乐的例子) 也可以返回多个值,以元组的方式进行保存
def mul(a=1, b=2, c=3, d=4):
    return a * b, c * d


print(mul(), type(mul()))

# 同时还要分清楚变量的作用域
ddd = 0  # 定义一个变量ddd 为全局变量


def aa():
    global ddd
    ddd = 3


def bb(a, b):
    ddd = a + b
    print("函数bb中的ddd值为{}".format(ddd))  # 这个ddd是内部的ddd 并不是全局变量
    return ddd


bb(2, 6)
print(ddd)  # 因为调用的是bb,而它内部的ddd并不是当前范围内的全局变量
aa()  # 调用函数 以改变全局变量的值
print(ddd)  # 打印全局变量的值 因为函数中获取到的全局变量被修改了值 所以打印的值已经不是初始值了

# 如果全局变量是一个列表会进行更改
# 具体查看6.2.1内容 列表等组合数据类型由于操作多个数据,所以他们在使用中具有创建和引用的区别  当前列表被方括号[]赋值时,这个列表才被真实创建,否则只是对前列表的一次引用
ls = []


def changeLs(num=3):
    ls.append(num)  # 这一行代码执行的时候需要一个已经创建过切名字为ls的列表,函数中没有对应的列表 则会去外一层(这个例子是全局)中寻找内存空间
    # 也就是说,对于列表类型 函数可以直接使用全局列表而不需要使用global进行声明 如果函数内部已经有了对应的列表则会优先修改函数内部对应的列表


print(ls)
changeLs(5)
print(ls)


def changeLs1(num=3):
    ls = [5, 6, 4]
    ls.append(num)  # 如果前面有定义ls则会优先使用函数中的ls
    print(ls)


changeLs1()
print(ls)  # 这个ls和函数内部的ls没有关系
