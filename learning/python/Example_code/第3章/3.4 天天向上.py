'''
    @Time : 2020/5/30 14:54 
    @Author : Mao Yuhuan
    @FileName : 3.4 天天向上
    @Software: PyCharm
'''

import math


def pr(fl):
    dayup = math.pow((1 + fl), 365)
    daydown = math.pow((1 - fl), 365)
    print("向上: {:.2f}, 向下: {:.2f}.".format(dayup, daydown))


pr(0.001)
pr(0.005)
pr(0.01)
pr(0.1)

day, dayFac = 1.0, 0.01
for i in range(365):
    if i % 7 in [6, 0]:
        day *= (1 - dayFac)
    else:
        day *= (1 + dayFac)
print("up five days and down two days: {:.2f}".format(day))
