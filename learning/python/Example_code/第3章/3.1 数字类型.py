'''
    @Time : 2020/5/26 12:31 
    @Author : Mao Yuhuan
    @FileName : 3.1 数字类型
    @Software: PyCharm
'''

# 可以进行值的计算
# print(pow(2, 100))
# print(pow(2, 500))
# print(pow(2, pow(9, 2)))

# 导入sys包
import sys

# 打印信息
print(sys.float_info)
print(sys.float_info.max)

print(3.14159265358979323846)  # 存在丢失的情况
print(123456789123456789.233333333)  # 会用科学计数法进行表示 表示有丢失

print(1.23456789 * 1.23456789)  # 使用浮点数进行运算 存在精度丢失
print(123456789 * 123456789)  # 去掉小数点 当成整数进行运算 不存在精度丢失

# 引入decimal库, 提供了更精确的数字类型Decimal
# 并且可以使用getcontext().prec 参数自定义浮点数精度的位数
import decimal

# 浮点数精度为2.20*10的-16次 对绝大多数运算来说足够可靠
a = decimal.Decimal('3.1415926535897')
b = decimal.Decimal('1.23456789')
decimal.getcontext().prec = 25
print(a * b)

# 复数 复数单位:j  j**2 = -1 表示为 a + bj
# 获取可以使用 z.real 和 z.imag 获取到复数z的实部和虚部
print((1.23e-4+5.67e+89j).real)
print((1.23e-4+5.67e+89j).imag)


