'''
    @Time : 2020/5/31 17:59 
    @Author : Mao Yuhuan
    @FileName : 3.15 填表四
    @Software: PyCharm
'''

for i in range(1, 11):
    score = 1.0
    for j in range(360):
        if j % 30 <= 10:
            score *= (1 + 0.001 * i)
    print("增加水平{:.3f}的结果为:{:.3f}".format(i*0.001, score))


