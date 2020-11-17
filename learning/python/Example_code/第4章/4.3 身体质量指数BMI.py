# -*- coding: utf-8 -*-
# @Time : 2020/7/3 2:37
# @Author : MYH
# @File : 4.3 身体质量指数BMI.py
# @Software: PyCharm

import math

# 身体质量指数BMI
height, weight = eval(input("请输入身高和体重[用逗号,隔开, \
身高单位m,体重单位kg]"))
# height, weight = input("请输入身高和体重").split(',')       # 用这个方式会输入两个变量 以字符串的形式
bmi = weight / math.pow(height, 2)
print("这个同学的BMI指数为: {:.2f}".format(bmi))
who, dom = "", ""  # 定义两个变量赋以空值
# 国际标准
if bmi < 18.5:
    who = "偏瘦"
elif bmi < 25:
    who = "正常"
elif bmi < 30:
    who = '偏胖'
else:
    who = '肥胖'

# 国际标准
if bmi < 18.5:
    dom = "偏瘦"
elif bmi < 24:
    dom = "正常"
elif bmi < 28:
    dom = '偏胖'
else:
    dom = '肥胖'

print("BMI指标为: 国际{} 国内{}".format(dom, who))

# 赋值可以改成 who, dom = "正常", "正常" 的形式 更加简便
# 这个第9行末尾的\的作用是: 代码可以换行写,不改变原意
