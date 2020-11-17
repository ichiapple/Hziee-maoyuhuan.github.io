'''
    @Time : 2020/5/31 18:01 
    @Author : Mao Yuhuan
    @FileName : 3.5 字符串类型及操作
    @Software: PyCharm
'''

# 字符串类型表示
print("单双'引号'可以进行嵌套")

print(input("请输入一个'数字': "))

# 字符串输出格式的使用
name = input("请输入一个长一点的人名: ")
print(name[0], name[2], name[6])
print(name[2:-4])
print(name[:6])
print(name[6:])
print(name[:])

# 转义字符的使用
print("\'\"Python\"\n\t语言\t程序\\设计\'")

# Python中对字符串的基本操作
print("Python" + " Hello" + " World")  # 字串连接
print("Go!" * 3)  # 可以对字串进行重复输出
name = "zhangsan"
print("Python" in name)  # 可以是字串对变量
print("y" in "Python")  # 可以是字串对字串

# 3.1 获取星期字符串
weekStr = "星期一星期二星期三星期四星期五星期六星期日"
week = eval(input("请输入一个数字1-7: "))
pos = week * 3 - 3  # 定位到字符串的位置
print(weekStr[pos:pos + 3])

# print('\a')   # 特殊格式输出
# 但是idle中不支持部分的字符

# 3.1* 获取月份 常用.
monthStr = "123456789101112"
month = eval(input("请输入一个数字1-12: "))
if month >= 10:
    monthStrpos = (month - 10) * 2 + 9  # 定位到字符串的位置
    print(monthStr[monthStrpos:monthStrpos + 2])
else:
    monthStrpos = month - 1  # 定位到字符串的位置
    print(monthStr[monthStrpos:monthStrpos + 1])

# python内置字符处理函数
print(len("Hello World"))# 计算字符串的长度
print(str(123456))# 输出数字到字符

# Unicode输出
print("1 + 1 = 2 "+chr(10004))
print("金牛座的符号是" + chr(9801))
print("字符'k'的Unicode值为: " + str(ord("k")))

# 3.2 凯撒密码
plainCode = input("请输入明文: ")
for p in plainCode:
    if ord("a") <= ord(p)<=ord("z"):
        print(chr(ord("a")+(ord(p)-ord("a")+3)%26), end='')       #  凯撒密码是右移三位获得
    else:
        print(p,end='')

# 内置字符串的处理方法
str = "asdfASDF123"
print(str.islower())  # 判断一个字符串是否都是小写字符
print(str.isupper())  # 判断一个字符串是否都是大写字符
print(str.isalnum())  # 判断一个字符串是否都是数字字串
print(str.isspace())  # 判断一个字符串是否都是空格
print(str.upper())  # 修改字符串为大写
print(str.lower())  # 修改字符串为小写
print(str.title())  # 修改字符串单词第一位大写 剩余小写
print(str.capitalize())  # 只修改字符串第一位大写 剩余小写

str1 = "asd-fgh-jkl-jk-kljkl-asd"
print(str1.endswith("kl"))  # 以..结束
print(str1.startswith("ss"))  # 以..开始
print(str1.split("-"))  # 返回一个列表 为分离后的数组
print(str1.count("kl", 1, -1))  # 返回kl子串出现的次数 后两个为起始位置和结束位置
print(str1.replace("jk", "kkk"))  # 用后者替代前者
print(str1.strip("asd"))  # 拷贝一份字串 去掉左右两侧的字串
print(str1.zfill(60))  # 拷贝一份 长度为60 不是的部分在左侧添加0    有问题
# format函数 join函数 会在3.6和第6章中讲

print(hex(255))
print(oct(-255))
print("Python is a good language!".split())
print("Python".center(40, "="))
print("123".zfill(40))
print("-123".zfill(5))
