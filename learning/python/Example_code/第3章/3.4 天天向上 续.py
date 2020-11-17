'''
    @Time : 2020/5/30 15:19 
    @Author : Mao Yuhuan
    @FileName : 3.5 天天向上 续
    @Software: PyCharm
'''


def dayDayUp(fl):
    day_up_value = 1.0
    for i in range(365):
        if i % 7 in [6, 0]:
            day_up_value *= (1 - 0.01)
        else:
            day_up_value *= (1 + fl)
    return day_up_value


dayFactory = 0.01
while dayDayUp(dayFactory) < 37.78:
    dayFactory += 0.001
print("每天的努力参数为: {:.3f}".format(dayFactory))
