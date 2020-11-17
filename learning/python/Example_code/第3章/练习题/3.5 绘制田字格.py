'''
    @Time : 2020/6/18 20:18 
    @Author : Mao Yuhuan
    @FileName : 3.5 绘制田字格
    @Software: PyCharm
'''

for i in range(21):
    s = ''
    if i%10==0:
        for j in range(21):
            if j % 10 == 0:
                s += '+'
            else:
                if j % 2 == 1:
                    s += ' '
                else:
                    s += '-'
    else:
        if i % 2 == 0:
            for j in range(21):
                if j % 10 == 0:
                    s += '|'
                else:
                    s += ' '
        else:
            print("")
    print(s,end='')
