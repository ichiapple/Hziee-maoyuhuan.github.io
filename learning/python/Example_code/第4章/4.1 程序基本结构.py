'''
    @Time : 2020/6/18 21:51 
    @Author : Mao Yuhuan
    @FileName : 4.1 程序基本结构.py
    @Software: PyCharm
'''

import math

# 计算圆面积和周长
r = eval(input("请输入圆半径: "))
S = r*r*math.pi
L = 2*math.pi*r
print("圆的面积和周长为:{:.3f}和{:.3f}".format(S,L))

# 绝对值的代码实现
a = eval(input("请输入一个数: "))
if a < 0 :
    a = -a
print(a,end='')

# 计算累加求和
a = eval(input("请输入一个整数:"))
i = 1
sum = 0

while i <= a:
    sum += i
    i += 1

print(sum)
