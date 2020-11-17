# -*- coding: utf-8 -*-
# @Time : 2020/7/3 21:59
# @Author : MYH
# @File : 4.6 羊车门问题.py
# @Software: PyCharm

# 假设一开始选中的是车，主持人指出其中一只羊之后，那么剩下的一个门也必定是羊，那么此时更改选择必定是得不到车的，这是第一种
# 假如一开始选中的是羊，在主持人指出一只之后，无论如何更改选择都是可以得到车的，所以有两种情况更改是ok的
# 所以是2/3。

from random import *
time = 10000
isT, isF = 0,0      # 保持初始选择 和 修改初始选择
for i in range(time):
    inDoor = randint(0,2)
    myGuess = randint(0,2)
    if inDoor == myGuess:
        isT+=1
    else:
        isF+=1
print("不更改选择和更改选择猜对的几率分别为 {} 和 {}".format(isT/time,isF/time))

# 例程
# from random import *
#
# TIMES = 10000
# my_first_choice_n = 0  # 初始化不改选择的次数
# my_change_choice_n = 0  # 初始化更改选择的次数
# for i in range(TIMES):
#     car_inDoor = randint(0, 2)
#     my_guess = randint(0, 2)
#     if car_inDoor == my_guess:
#         my_first_choice_n += 1
#     else:
#         my_change_choice_n += 1
# print("不改选择:{}".format(my_first_choice_n / TIMES))
# print("更改选择:{}".format(my_change_choice_n / TIMES))
