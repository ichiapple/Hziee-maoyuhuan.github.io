'''
    @Time : 2020/6/1 0:32 
    @Author : Mao Yuhuan
    @FileName : 3.16 字符串分离
    @Software: PyCharm
'''

s = "hello"
t = "world"
s += t

print(s)
print(s[-1])
print(s[2: 8])  # 从2读取到8
print(s[::3])  # 步进为3
print(s[-2::-1])  # s[0::-2] 进行反转展示

print(s[::-1])  # 字符串反转
print(s[8:4:-1])  # 字符串反转 从下标为2的字符读取到4 步进为-1
