# -*- coding: utf-8 -*-
# @Time : 2021/3/3 13:34
# @Author : MYH
# @File : demo_简单获取数据.py
# @Software: PyCharm

# 导入所需要的库
from urllib import request, parse

# 设置需要访问的网页
# url = "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="

# 不设置User-Agent直接访问网站 部分设置了反爬虫的网站会返回简短的信息而非原网页
# resp = request.urlopen(url)
# print(resp.read())

# 使用User-Agent,让网站认为是普通人在进行访问
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"}
# req = request.Request(url,headers=headers) # 封装好request对象
# resp = request.urlopen(req) # 将设置好的额request对象放入,进行访问
# print(resp.read()) # 但是发现页面中没有想要的数据 页面数据通过另外的请求进行获取后追加到此页面中的

# 通过搜索请求发现,数据访问的是另一个请求
# data_url = "https://www.lagou.com/jobs/positionAjax.json?city=%E6%9D%AD%E5%B7%9E&needAddtionalResult=false"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
#     "Referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="
# }
# data = {"first": "true", "pn": 1, "kd": "python"}  # 设置请求参数
# req = request.Request(data_url, headers=headers, data=data, method='POST') # 这样请求会报错 "can't concat str to bytes" 需要urlencode
# req = request.Request(data_url, headers=headers, data=parse.urlencode(data), method='POST') # 仍然报错,需要将unicode字符串转换为字节流(byte)
# req = request.Request(data_url, headers=headers, data=parse.urlencode(data).encode("utf-8"),
#                       method='POST')  # 获取成功 可能返回操作过频繁错误
# resp = request.urlopen(req)
# print(resp.read().decode("utf-8"))  # decode方法可以将字节流 b' 转换为unicode字符 包含了: "msg":"您操作太频繁,请稍后再访问"
# 但是事实上此msg为迷惑行为.在页面上可以正常访问或刷新 说明程序已经被识别为爬虫 需要进行伪造
