# 定义a和b为0和1
a, b = 0, 1

# 输出不大于1000的序列
while a < 1000:
    print(a, end=',')
    a, b = b, a + b
