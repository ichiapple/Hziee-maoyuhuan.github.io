'''
    @Time : 2020/6/7 0:56 
    @Author : Mao Yuhuan
    @FileName : 3.7 文本进度条
    @Software: PyCharm
'''

# # 简单的文本进度条
# import time
#
# scale = 30
#
# print("Bein..")
#
# for i in range(scale + 1):
#     a, b = "**" * i, "--" * (scale - i)
#     c = (i / scale) * 100
#     print("{:^3.0f}% [{}->{}]".format(c, a, b))
#     time.sleep(0.5)
#
# print("End..")

# # 单行动态刷新
# import time
#
# for i in range(101):
#     print("\r{:3}%".format(i), end=" ")
#     time.sleep(0.4)

# 带刷新功能的文本进度条
import time

scale = 30
t = time.clock()  # 会爆警告 因为在3.3版本以后就不建议使用了
print("Begin..".center(scale // 2, "-"))  # 使用center函数将文本放置在中间 旁边使用-代替 一共为一半的scale长度

for i in range(scale + 1):
    a = "*" * i  # 前面的字符串
    b = '-' * (scale - i)  # 后面的字符串
    c = (i / scale) * 100  # 计算百分比
    t -= time.clock()  # 计算时间 使用-=计算  计算的是本次调用和上次调用之间的时间差
    print("\r{:^3.0f}% [{}->{}] {:.2f}s".format(c, a, b, -t), end='')  # 注意这里要打印的是-t
    time.sleep(0.05)

print("\n" + "End..".center(scale // 2, "-"))  # 同上理
