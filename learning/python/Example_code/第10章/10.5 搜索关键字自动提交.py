# -*- coding: utf-8 -*-
# @Time : 2020/7/12 3:33
# @Author : MYH
# @File : 10.5 搜索关键字自动提交.py
# @Software: PyCharm

# 当用百度进行查找的时候,会出现 类似https://www.baidu.com/s?ie=UTF-8&wd=%E7%99%BE%E5%BA%A6 的url 我们可以将关键词进行替换实现查找
# 输入: 查找的内容 处理: 自动获取百度搜索页面,并对页面进行处理 输出: 返回链接标题列表

# 导入部分
import requests
from bs4 import BeautifulSoup
import json
import re  # 正则表达式库


def getKeywordSearch(keyword):
    url = 'http://www.baidu.com/s?wd=' + keyword
    print("正在进行访问的网址为:{}".format(url))
    # print(url) # 测试输出
    try:
        r = requests.get(url, timeout=100)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""


def parseLinks(html):
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.text)
    links = []
    for div in soup.find_all('div', {'data-tools': re.compile('title')}):
        data = div.attrs['data-tools']  # 获得属性值
        # print(data)  # 测试data输出
        d = json.loads(data)  # 将属性值转换为字典
        links.append(d['title'])  # 将返回链接的题目返回
        links.append(d['url'])  # 将链接返回
    return links


def main():
    html = getKeywordSearch("Python")
    # print(html)
    ls = parseLinks(html)
    count = 0
    for i in ls:
        count += 1
        print("{:^3} -> {}".format(count if count %2!=0 else "", i))


main()

# captcha验证码: 该验证码是"全自动区分计算机和人类的图灵测试"的缩写 能够区分是人还是电脑,防止程序恶意向网络自动提交请求
# 该验证码的原理是通过图片或者语音的方式展现人类容易识别但是程序难识别的内容 对反馈的内容进行判断是人类还是程序 该验证码已经成为现代网络服务系统的标准配置

# 能力越大,责任越大

