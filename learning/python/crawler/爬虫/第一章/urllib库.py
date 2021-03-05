# -*- coding: utf-8 -*-
# @Time : 2021/3/1 11:37
# @Author : MYH
# @File : urllib库.py
# @Software: PyCharm

# 统一导入库
from urllib import request, parse

# urlopen函数 演示
# resp = request.urlopen('http://www.baidu.com')
# print(resp.read())  # 获取网页源代码并输出 参数可以指定读取多少字符
# print(resp.readlines()) # 网页内容以多行形式进行输出
# print(resp.getcode())  # 获取状态码并输出

# urlretrieve函数 演示
# request.urlretrieve('http://www.baidu.com','baidu.html')

# urlencode函数 演示
# data = {'name': "爬虫基础", "greet": "Hello world", "age": 23}
# qs = parse.urlencode(data)
# print(qs)  # 将转换好的编码输出 name=%E7%88%AC%E8%99%AB%E5%9F%BA%E7%A1%80&greet=Hello+world&age=23

# parse_qs函数 演示
# from urllib import parse
# qs_str = "name=%E7%88%AC%E8%99%AB%E5%9F%BA%E7%A1%80&greet=Hello+world&age=23"
# print(parse.parse_qs(qs_str))

# 为什么要使用转码后的文本进行访问 不转码测试
# request_str = "https://www.baidu.com/s?"
# req_str = request_str + 'wd=你好李焕英'
# resp = request.urlopen(req_str)
# print(resp.read()) # 报错 表示不能访问
# req_str = request_str + parse.urlencode({"wd": "你好李焕英"})
# resp = request.urlopen(req_str)
# print(req_str)
# print(resp.read()) # 可以访问

# urlparse和urlsplit函数
# url1 = 'http://www.baidu.com/s?username=zhiliao'
# url2 = 'http://www.baidu.com/s;hello?username=zhiliao'
# # result = parse.urlsplit(url)
# result = parse.urlparse(url1)  # 两种方式都是可以的
# print('scheme', result.scheme)
# print('netloc', result.netloc)
# print("path", result.path)
# print("query", result.query)
# print("params", result.params)  # 1 2 在这里有区别
# print("fragment", result.fragment)

# ProxyHandler的使用
resp = request.urlopen("http://httpbin.org/get")  # 不适用代理进行访问
print(resp.read().decode("utf-8"))
handler = request.ProxyHandler({"http":"218.66.161.88:31769"})