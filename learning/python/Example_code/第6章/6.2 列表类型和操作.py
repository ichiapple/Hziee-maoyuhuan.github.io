# -*- coding: utf-8 -*-
# @Time : 2020/7/4 22:29
# @Author : MYH
# @File : 6.2 列表类型和操作.py
# @Software: PyCharm

# 列表是包含0个或者多个对象引用的有序序列,没有长度限制,可以自由增删元素,使用灵活
ls = [425, "BIT", [10, "cs"], 425]
print(ls)
print(ls[2][1][1])
print(list("中国是一个伟大的国家"))  # 每一个字符都会作为列表项

# 列表和数组:
# 都是表示一组元素的方法 但是在C语言中采用的是数组,而在Python中则使用的是列表
# 主要有两个区别: 数组需要预先分配大小,而列表则不需要 数组的数据类型需要一致,但是列表却不需要(因为这个特点而比较灵活,为程序编写有很大的空间)

# 列表必须通过显式数据赋值才可以生成,简单将一个列表赋值给另一个列表则不会产生新的列表
lt = ls
print(lt[3])
lt[0] = 999  # 因为简单将一个列表赋值给另一个列表不会创建一个新的列表,所以ls和lt其实是同一个列表,修改lt则是修改ls
print(ls)

# 列表类型的操作
# ls[i] = x                   将x赋值给ls的下标为i的元素
# ls[i:j] = lt                将ls下标congi开始到j(不含j)的字串替换成lt
# ls[i:j:k] = lt              将ls下标congi开始到j(不含j) 步进为k的元素替换成lt
# del ls[i:j]                 删除从ls下标从i开始到j(不含j) 相当于ls[i:j]=[]
# del ls[i:j:k]               删除从ls下标从i开始到j(不含j)步进为k的元素相当于ls[i:j:k]=[]
# ls+=lt 或者 ls.extend(lt)    将列表lt中元素添加到ls中
# ls *= n                     更新列表ls,其元素重复n次
# ls.append(x)                在ls后追加元素x
# ls.clear()                  清空ls
# ls.copy()                   生成一个ls的拷贝
# ls.insert(i,x)              在列表i位置插入元素x
# ls.pop(i)                   从ls中取出元素i 并从列表中删除该元素
# ls.remove(x)                从列表ls中删除x元素
# ls.reverse()                将ls中的元素反转

vls = list(range(10))
print(vls)
print(len(vls[3:]))  # 计算从vls下标为3的位置开始到结尾有多少个元素
print(3 in vls)
vls[5] = 'Python'
print(vls)
print(vls[4:6])
vls[4:6] = "nihao", "shijie"
print(vls)
vls[4:6] = "Hello"  # 会认为每一个字符就是一个元素
print(vls)
vls[4:6] = "22", "555", "999"
print(vls)

for it in vls:
    print(it, end=' ')
