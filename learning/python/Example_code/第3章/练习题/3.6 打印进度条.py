'''
    @Time : 2020/6/18 20:54 
    @Author : Mao Yuhuan
    @FileName : 3.6 打印进度条
    @Software: PyCharm
'''


import time
t = time.clock()


for i in range(7):
    a = '.'*i
    b = ' '*(7-i)
    t -=time.clock()
    print('\r{} {}{}'.format("Starting",a,b),end='')
    time.sleep(0.6)

print("Done",end='')