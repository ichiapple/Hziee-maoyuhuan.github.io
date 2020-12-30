# -*- coding: utf-8 -*-
# @Time : 2020/12/31 0:37
# @Author : MYH
# @File : 文件夹下文件批量处理.py
# @Software: PyCharm
import os

from PIL import Image

for path, obj, lists in os.walk("test"):  # 读取文件夹下所有文件 获取方式: 拆包
    print(path)  # 本文件夹名
    print(obj)  # 子文件夹名
    print(lists)  # 文件列表(数组)
    print("---- 分隔符 ----")
    for i in lists:  # 进行批量重命名
        test_name = os.path.splitext(i)[0]+".png"
        Image.open(path+'/'+i).save(path+'/'+test_name) # 打开并保存 如果遇到有其他文件则会报错
