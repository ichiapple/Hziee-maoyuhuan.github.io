'''
    @Time : 2020/5/26 10:29 
    @Author : Mao Yuhuan
    @FileName : 2.2 兑换money
    @Software: PyCharm
'''

a = input("请输入一个以C或U结尾的值: ")

if a[-1] in ['C','c']:
    print(eval(a[0:-1])//6)
elif a[-1] in ['U', 'u']:
    print(eval(a[0:-1])*6)
else:
    print("输入错误")
