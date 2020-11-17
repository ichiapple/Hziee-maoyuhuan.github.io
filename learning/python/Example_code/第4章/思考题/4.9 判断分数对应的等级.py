# -*- coding: utf-8 -*-
# @Time : 2020/7/3 2:33
# @Author : MYH
# @File : 4.9 判断分数对应的等级.py
# @Software: PyCharm

# 分析程序 如果score为80 则输出的grade是多少
# 书上代码 有问题 应该把大范围的条件放到前面 小范围放后面 这题恰恰相反了
score = eval(input("请输入score"))
if score >=60:
    grade = 'D'
elif score>70:
    grade = 'C'
elif score > 80:
    grade = 'B'
elif score>90:
    grade = 'A'
else:
    grade = 'E'

print(grade)