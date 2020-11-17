'''
    @Time : 2020/5/31 17:57 
    @Author : Mao Yuhuan
    @FileName : 3.14 填表三
    @Software: PyCharm
'''

for i in range(1, 11):
    score = 1.0
    for j in range(365):
        if j % 7 not in [0]:
            score *= (1 + 0.001 * i)
    print("增加水平{:.3f}的结果为:{:.3f}".format(i * 0.001, score))
