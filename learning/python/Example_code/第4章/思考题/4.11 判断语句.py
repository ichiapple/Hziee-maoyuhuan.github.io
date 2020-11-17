# -*- coding: utf-8 -*-
# @Time : 2020/7/3 13:05
# @Author : MYH
# @File : 4.11 判断语句.py
# @Software: PyCharm

print(24<=28<25)        # false
print(22<=24<25)        # false

# 这是因为左结合性 并且<的优先级高于<= 所以先会计算28<25答案为1 24<=1当然就不成立了 所以答案为false
