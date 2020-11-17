# -*- coding: utf-8 -*-
# @Time : 2020/7/4 17:52
# @Author : MYH
# @File : 5.7 汉诺塔问题.py
# @Software: PyCharm

# 采用递归方法解决问题
# 1层>1次 2层>3次 3层>7次 后一次是前一次的两次加一

# def hannuo(n):
#     if n == 1:
#         return 1
#     else:
#         return hannuo(n - 1) * 2 + 1
#
#
# print(hannuo(64))  # 打印出来的是汉诺塔问题的移动次数

# 例程
# class Hanoi:
#     def getSolution(self, n):
#         # write code here
#         self.ans = []
#         self.hanoi(n, "left", "mid", "right")
#         return self.ans
#
#     def hanoi(self, n, left, mid, right):
#         if n == 1:
#             self.move(left, right)
#             return
#         # 将前 n - 1 个盘子从 left 移动到 mid
#         self.hanoi(n - 1, left, right, mid)
#         # 将最底下的最后一个盘子从 left 移动到 right 上
#         self.move(left, right)
#         # 将 mid 上的 n - 1 个盘子移动到 right 上
#         self.hanoi(n - 1, mid, left, right)
#
#     def move(self, A, B):
#         self.ans.append("move from " + A + " to " + B)
#
#
# if __name__ == "__main__":
#     a = Hanoi()
#     print(a.getSolution(3))

; # 有问题

def hannuoSe(n):
    if n == 1:
        recordStep('left','right')
        return 1
    else:
        hannuoSe()
        return hannuoSe(n - 1) * 2 + 1


def recordStep(left, right):
    print("MOVE FROM " + left + " TO " + right)
