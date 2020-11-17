'''
    @Time : 2020/5/30 15:41 
    @Author : Mao Yuhuan
    @FileName : 3.13 填表二
    @Software: PyCharm
'''

for i in range(1, 11):
    score = 1.0
    for j in range(365):
        if j % 7 not in [6, 0]:
            score *= (1 + 0.001 * i)
    print("增加水平{:.3f}的结果为:{:.3f}".format(i*0.001, score))
