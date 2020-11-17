# 输入
n = input("请输入一个整数: ")

# 初始化
sum = 0     # 结果初始化为0

# 计算 i从0开始 所以下面要加一
for i in range(int(n)):
    sum += i+1

# 输出
print("1到N的结果为: {}".format(sum))