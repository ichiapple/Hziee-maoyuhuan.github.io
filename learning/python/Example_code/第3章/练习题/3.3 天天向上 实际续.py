'''
    @Time : 2020/6/7 1:34 
    @Author : Mao Yuhuan
    @FileName : 3.2 天天向上 实际
    @Software: PyCharm
'''

days = 365
ablity = 1
space = 10
mark = 0

for i in range(days + 1):
    if i % space == 0:
        mark = 0
    else:
        mark += 1
    if mark % 7 in [0, 1, 2]:
        ablity = ablity
    elif mark % 7 in [3, 4, 5, 6]:
        ablity *= 1.01
    else:
        print("Error..")
    if mark % 7 == 6:
        mark = 0

print(ablity)
