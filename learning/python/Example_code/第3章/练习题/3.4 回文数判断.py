'''
    @Time : 2020/6/7 2:02 
    @Author : Mao Yuhuan
    @FileName : 3.4 回文数判断
    @Software: PyCharm
'''

# 这个是自己想的,没想出来
# s = "giuig"
# length = len(s)
# chk = 0
#
# for i in range(length):
#     # print("{0},{1}".format(s[i],s[-i]))
#     if s[i] == s[-i]:
#         continue
#     if i > length - 1:
#         chk = 1
#     else:
#         break
#
# if chk == 1:
#     print("是回文数")
# else:
#     print("不是回文数")


# 输入字串
a = input('请输入一个数')
# 进行逆序输出存入变量b
b = a[::-1]
if a == b:
    print('这是回文数')
else:
    print('这不是回文数')
