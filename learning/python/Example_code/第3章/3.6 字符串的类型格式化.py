'''
    @Time : 2020/6/2 0:03 
    @Author : Mao Yuhuan
    @FileName : 3.6 字符串的类型格式化
    @Software: PyCharm
'''

# 内容会变化 需要用特定函数进行填充 建议使用该方法
# 参数依照顺序填充到模板字符串中的{}中
# 如果大括号中没有序号, 则按照出现的顺序进行替换

print("{}{}{}".format("I ", "LOVE ", "YOU"))
print("PI的{1}为{0}".format(3.14159,"值"))
s = "圆周率{{{1}{2}}}的值为{0}"
print(s)
print(s.format("无理数", "3.1415926", "..."))  # format解析的是{}

# format()函数中不仅可以替换{}中的数字 还有其他控制信息
# :引导符号 <用于填充的单个字符>  <左对齐 >右对齐 <宽度>  <千分位分隔符> <精度(浮点数 字符串)> <类型>
p = "Python"
print("{0:30}".format(p))# 默认左对齐 占30个位置
print("{0:>30}".format(p))# 右对齐 占30个位置
print("{0:*^30}".format(p))# 居中 用* 填充
print("{0:-^30}".format(p))# 居中 用- 填充
print("{0:3}".format(p))# 格式不受控制

# 千分位表示
print("{0:*^20,}".format(123456789))
print("{0:*^20}".format(123456789))
print("{0:*^20,}".format(1234.56789))

# 精度表示两个含义: 对于浮点数,输出格式表示小数的输出位数 对于字符串 表示输出的最大长度
print("{0:.2f}".format(12345.6789))     # 保留两位小数 四舍五入
print("{0:H^20.3f}".format(123456.67890)) # 长度为20 用H代替两边 中间放置字串 长度为保留三位
print("{0:.4}".format("Python")) #字符串输出最长长度为4位

# 类型 表示输出的格式规则
# b 表示二进制
# c 表示整数对应的Unicode字符
# d 输出整数的十进制方式
# o 输出整数的八进制方式
# x 输出整数的小写十六进制
# X 输出整数的大写十六进制
print("{0:b},{0:c},{0:d},{0:o},{0:x},{0:X}".format(3493))
# 对于浮点数, 有四种输出格式
# e 输出浮点数对应的小写e的指数形式
# E 输出浮点数对应的大写E的指数形式
# f 输出浮点数对应的标准浮点形式
# % 输出浮点数对应的百分形式
print("{0:e},{0:E},{0:f}{0:%}".format(3.14))
print("{0:.2e},{0:.2E},{0:.2f}{0:.2%}".format(3.14))


