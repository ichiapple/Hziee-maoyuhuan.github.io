'''
    @Time : 2020/5/24 23:45
    @Author : Mao Yuhuan
    @FileName : 123
    @Software: PyCharm
'''

# Python中采用严格的缩进 可以嵌套无限制使用
# 有缩进的行为前一个无缩进代码行管辖范围

# 单行注释使用 "# "+文本

'''
print(2)
这里是多行注释 不会被计算机执行
'''

# python中变量大小写敏感 Aa 和 aa 为两个变量 for保留字 For可以用

# Python中字符串 正向str[0~n-1] 逆向str[-1~-n]
# 字串区间访问方式 [N,M]表示方法 从N到M(不含M) 可以混用
str = "1100C"
print(str[-1])
print(str[0:-2])

# 赋值语句
x = 1
y = 2
x, y = y, x  # 可以这样写 同步赋值 相对别的语言引入中间变量简洁
print("x:{}".format(x))
print("y:{}".format(y))

# input函数
# print函数

# 分支语句
if x > 1:
    print("大于1")
elif x > 0:
    print("大于0")
else:
    print("小于等于0")

# eval 函数 能够以python的方式解析并执行字符串 并将返回结果输出
x = 1
print(eval("x + 1"))
print(eval("1.1 + 2.2"))  # 有精度丢失的情况
TempStr = "1022C"
print(eval(TempStr[0:-2]))

# print(eval("hello"))        # 会报错 因为不能将hello解析为一个变量
print(eval("'hello'"))  # 会将'hello'解析成一个字串

a = eval(input("请输入一个数: "))
print(a ** 2)

# 判断语句
arr1 = [1, 2, 3]
i = 2
if i not in arr1:
    print("i不在数组中")
else:
    print("i在数组中")

# 循环语句
while i < 4:
    print(i)
    i += 1


# 定义函数
def temp_convert(value):
    if value[-1] in ['F', 'f']:
        C = (eval(value[0: -1]) - 32) / 1.8
        print("转换后的结果为: {:.2f}C".format(C))
    elif value[-1] in ['C', 'c']:
        F = (eval(value[0: -1])) * 1.8 + 32
        print("转换后的结果为: {:.2f}F".format(F))
    else:
        print("输入格式错误.")


value = input("请输入一个带符号的温度: ")  # 获取值
temp_convert(value)  # 调用函数
