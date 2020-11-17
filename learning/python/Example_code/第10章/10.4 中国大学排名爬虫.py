# -*- coding: utf-8 -*-
# @Time : 2020/7/12 2:30
# @Author : MYH
# @File : 10.4 中国大学排名爬虫.py
# @Software: PyCharm

# 大学排名爬虫,从网站上获取大学排名信息

# 导入部分
import requests
from bs4 import BeautifulSoup
import html5lib
import re  # 正则表达式库

alluniv = []  # 存储全部表格数据的二维列表


def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""


def filllUnivList(soup):
    data = soup.find_all('tr')  # 找到所有的tr标签
    for tr in data:  # 对每一个tr进行遍历,获取数据
        singleuniv = []  # 单行列表,初值为空
        ltd = tr.find_all('td')
        if len(ltd) == 0:
            continue  # 如果这一行为空则进行下一行数据的获取
        for td in ltd:  # 对每一个td进行遍历
            singleuniv.append(td.string)
        alluniv.append(singleuniv)  # 在总的二维表中添加一行数据


def printuniv(num):
    print("{:^4}{:^15}\t{:^10}{:^8}{:^10}".format("排名", '学校名称', '省份', '总分', '模块得分'))
    for i in range(num):
        u = alluniv[i]  # 对每一行进行遍历,获取数据存储到u中
        print("{:^4}{:^15}\t{:^10}{:^8}{:^10}".format(u[0], u[1], u[2], u[4], u[5]))
        # print('{:^4}[{name:<{len}}\tx{:^15}{:^8}{:^10}'.format(u[0],(name=u[1] + ']', len=22 - len(u[1].encode('GBK')) + len(u[1]), u[2], u[4], u[5]))
        # name=u[1] + ']', len=22 - len(u[1].encode('GBK')) + len(u[1]))

def main(num):
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2020.html'  # 设置需要爬取的网站
    html = getHtmlText(url)
    soup = BeautifulSoup(html, "html.parser")
    filllUnivList(soup)
    printuniv(num)


main(100)
