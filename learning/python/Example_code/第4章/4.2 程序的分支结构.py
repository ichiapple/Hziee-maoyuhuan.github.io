'''
    @Time : 2020/6/18 23:53 
    @Author : Mao Yuhuan
    @FileName : 4.2 程序的分支结构.py
    @Software: PyCharm
'''


# PM2.5提醒

# 第一种写法 包含了单分支if语句 if-elif-else if-else
# pm = eval(input("请输入PM2.5值:"))
# if 0<=pm<35:
#     print("空气优,可以活动")
# elif 35<=pm<=75:
#     print("空气良,注意防护")
# else:
#     print("空气污染 请小心")

# 第二种写法
pm = eval(input("请输入PM2.5值:"))
print("今天空气{}污染".format("存在" if pm >= 75 else "没有"))  # 这种简便写法: 表达式1 if 条件 else 表达式2

# 条件语句例子
# print(3<5)
# print("Hello"=="Hello")
# print("hello">"Hello")
