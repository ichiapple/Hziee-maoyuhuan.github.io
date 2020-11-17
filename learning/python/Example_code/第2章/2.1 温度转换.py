'''
    @Time : 2020/5/24 23:45
    @Author : Mao Yuhuan
    @FileName : 123
    @Software: PyCharm
'''

TempStr = input("请输入以C或者F结束符号的温度: ")

# 进行判断 最后一位字符  :.2f用于控制格式
if TempStr[-1] in ['F', 'f']:
    C = (eval(TempStr[0: -1]) - 32) / 1.8
    print("转换后的结果为: {:.2f}C".format(C))
elif TempStr[-1] in ['C', 'c']:
    F = (eval(TempStr[0: -1])) * 1.8 + 32
    print("转换后的结果为: {:.2f}F".format(F))
else:
    print("输入格式错误.")
