# -*- coding: utf-8 -*-
# @Time : 2021/3/3 13:02
# @Author : MYH
# @File : requests库.py
# @Software: PyCharm

import requests

# 使用requests进行简单get请求
# response = requests.get("http://www.baidu.com")
# print(response)  # 打印访问结果和状态码

# 添加headers和查询参数
keywords = {"wd": "中国"}  # 设置查询字符串
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"}  # 设置headers 的UA
response = requests.get("http://www.baidu.com/s", params=keywords, headers=headers)  # 设置请求
print(response) # 打印访问结果和状态码
print(response.text) # 打印响应内容 返回Unicode格式的数据 (可以理解为字节数据进行初步解码所得结果) 机器猜测,可能乱码
print(response.content) # 打印响应内容 返回字节流数据
print(response.url) # 打印访问URL 文本经过转码 第一次打印可能会转到webpass验证页面
print(response.encoding) # 打印响应头字符编码
print(response.status_code) # 打印状态码
with open("baiduWithKeywords.html", 'w', encoding="utf-8") as fp: # 将结果保存为文件
    fp.write(response.content.decode("utf-8")) # 不能直接写为文件,需要进行转码
