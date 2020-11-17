# 计算10的阶乘的和
# 初始化
res = 0
temp = 1

for i in range(1,11):
    temp*=i
    res+=temp
print("运算结果为: {}".format(res))
