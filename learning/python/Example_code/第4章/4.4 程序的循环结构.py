# -*- coding: utf-8 -*-
# @Time : 2020/7/3 14:16
# @Author : MYH
# @File : 4.4 程序的循环结构.py
# @Software: PyCharm

# 基本结构 从遍历结构中一一提取元素进行操作 其中else部分可选 是循环结束会执行的语句
# for <循环变量> in <遍历结构>:
#     <语句块1>
# else:
#     <语句块2>
# 遍历结构可以是字符串/文件/组合数据/range()范围

for s in "BIT":
    print("循环正在打印的是: "+s)
else:
    print("循环正常结束")

# 无限循环: while语句
# while <条件表达式>:
#     <语句块1>
# else:
#     <语句块2>
# else是附加功能,只有当while循环正常执行后才会执行else语句中的内容

s, index = "Hello",0
while index < len(s):
    print("循环正在打印的是: "+s[index])        # 打印的是对应字串位置的字母
    index+=1        # while不会自增所以为了避免死循环,故要将循环变量进行步进
else:
    print("循环结束")

# break和continue关键字 用于控制循环执行
# break用于控制跳出自己所在的那层循环  脱离后从循环代码后继续执行
# continue用于控制跳出自己所在的那次循环 然后继续进行下一次循环

for s in "Hello":
    for i in range(10):
        print(s,end='')     # 打印完进行判断 如果是l则进行跳出本层循环
        if s=='l':
            break

print() #换行 用于显示明显一点

# break和continue之间的比较
for s in "Python":
    if s == "t":
        continue
    print(s,end='')     # 打印出来 如果是t则已经在上一次进行continue操作 会跳过本行代码
else:
    print("正常退出",end='')

print() #换行 用于显示明显一点

for s in "Python":
    if s=='t':
        break
    print(s,end='')     # 打印出来 如果是t则进行break终止循环
else:
    print("正常退出",end='')        # 如果是break退出的则不会 执行else后的内容
