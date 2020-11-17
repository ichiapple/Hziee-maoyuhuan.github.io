'''
    @Time : 2020/5/26 17:39 
    @Author : Mao Yuhuan
    @FileName : 3..3 math函数库的使用
    @Software: PyCharm
'''

# 两种导入方法    math<>()   from math import floor

import math
from math import floor  # 这里使用import * 表示导入math包下的所有方法

# 打印值
print(math.pi)
print(math.e)
print(math.inf)
print(math.nan)

# math库函数演示
print(math.fabs(-6.3))
print(math.fmod(62, 7))
print(math.fsum([1, 3.321, 5.22, 6, 9, 2.11, 20]))  # 计算多个值的和 传入的参数有且仅能有一个
print(math.ceil(10.2))  # 向上取整
print(floor(10.2))  # 向下取整
print(math.factorial(6))  # 计算阶乘
print(math.gcd(12, 18))  # 计算两数的公约数
print(math.frexp(256))  # 返回m*2**r  返回(m,r)
print(math.ldexp(0.5, 9))  # 返回m*2**r 的值
print(math.modf(2.323))  # 返回小数和整数部分
print(math.trunc(2.323))  # 返回整数部分
print(math.copysign(3, -6))  # 用y的正负 替换x的正负
print(math.isclose(2.3, 2.30))  # 比较a和b的相似性
print(math.isfinite(math.nan))  # 当x不为无穷大或者NaN时返回True 否则返回False 有问题
print(math.isinf(math.inf))  # 如果无穷返回True 否则返回False
print(math.isnan(math.nan))  # 如果为NaN则返回True 否则返回False

print(0.1 + 0.2 + 0.3)
print(math.fsum([0.1, 0.2, 0.3]))  # 使用fsum函数进行运行时 精度准确
print("函数演示介绍完成")

# 幂对数函数
print(math.pow(10, 1 / 3))  # 返回x的y次幂
print(math.exp(2))  # 返回e的次幂
print(math.expm1(2))  # 返回e的x次幂减1
print(math.sqrt(100))  # 返回平方根
print(math.log(20, 3))  # 返回log(base)x 的对数值 其中如果只输入x则为ln(x)
print(math.log1p(3))  # 返回 1+x的对数值
print(math.log2(4))  # 返回x对2的对数值
print(math.log10(100))  # 返回x对10的对数值
print("高幂对数函数介绍完成")

# math库的三角函数运算
print(math.degrees(math.pi))  # 弧度值转换为角度值
print(math.radians(90))  # 角度值转换为弧度值
print(math.hypot(3, 4))  # 坐标(x,y)到坐标原点的距离
print(math.sin(30))  # 三角函数正弦
print(math.cos(30))  # 三角函数余弦
print(math.tan(30))  # 三角函数正切
print(math.asin(0.5))  # 三角函数反正弦
print(math.acos(0.5))  # 三角函数反余弦
print(math.atan(0.5))  # 三角函数反正切
print(math.atan2(12, 6))  # 返回 (y,x) 中 y/x 的反正切函数值
print(math.sinh(2))  # 三角函数双曲正弦函数
print(math.cosh(2))  # 三角函数双曲余弦函数
print(math.tanh(2))  # 三角函数双曲正切函数
print(math.asinh(0.5))  # 三角函数反双曲正弦函数
print(math.acosh(2))  # 三角函数反双曲余弦函数
print(math.atanh(0.5))  # 三角函数反双曲正切函数

print(math.atan(1) * 4)  # arctan(1)为pi/4
print("三角函数介绍完成")


# math库中的高等的特殊函数
print(math.erf(1))  # 高斯误差函数
print(math.erfc(1))  # 余补高斯误差函数
print(math.gamma(2))  # 伽马函数 欧拉第二积分函数
print(math.lgamma(2))  # 伽马函数的 自然对数
print("高等特殊函数介绍完成")
