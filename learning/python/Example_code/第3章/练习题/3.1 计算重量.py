'''
    @Time : 2020/6/7 1:28 
    @Author : Mao Yuhuan
    @FileName : 3.1 计算重量
    @Software: PyCharm
'''

t = 60.5

def addWeight(w):
    w += 0.5
    return w

for i in range(10+1):
    t = addWeight(t)
    print("地球上: {:.2f}".format(t))
    print("月球上: {:.2f}".format(t * 16.5 / 100))


