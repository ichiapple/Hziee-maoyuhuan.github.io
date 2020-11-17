# -*- coding: utf-8 -*-
# @Time : 2020/7/12 1:09
# @Author : MYH
# @File : 10.3 bs4库的使用.py
# @Software: PyCharm

# request库可以获取页面并转换成字符串,但是如果需要进一步处理则需要beautifulsoup4库
# bs4库将专业的web页面格式解析部分封装成函数,提供了若干有用便捷的处理函数 最大优点是能根据html或xml语法建立解析树 把页面当作对象,通过<a>.<b>()的方式调用方法(处理函数)
# 可以访问 https://www.crummy.com/software/BeautifulSoup/ 获取更多信息

# 导入部分
import requests
from bs4 import BeautifulSoup
import html5lib
import re  # 正则表达式库

# BeautifulSoup4库中最主要的是BeautifulSoup类,每个实例化的对象相当于一个页面,可以使用BeautifulSoup()方法创建一个对象
url = "http://www.baidu.com"
r = requests.get(url, timeout=30)
r.encoding = 'utf-8'  # 设置编码格式为utf-8
soup = BeautifulSoup(r.text, 'html5lib')  # soup就是一个beautifulsoup对象 指定解析器 这里使用新的解析器html5lib 因为使用lxml会报错
print(type(soup))  # 创建的soup对象是一个树形结构,包含页面的每一个tag(标签元素),元素都成为了soup对象的属性

# beautifulsoup对象的常用属性:
# head  # html页面的<head>内容
# title  # html页面的页面标题
# body  # html页面的<body>内容
# p  # html页面的第一个p标签内容
# strings  # html页面的字符串内容 即标签内容
# stripped_string  # html页面的所有非空格字符串

# print(soup.head)
# print(soup.title)
# print(type(soup.title))
# print(soup.p)  # 直接调用只能返回第一个 如果要找到所有标签则需要使用其他方法

# 找寻所有标签
# 格式:BeautifulSoup.find_all(name=,attrs=,recursive=,string, limit=)
# name(按照标签名检索) attrs(根据标签属性值进行检索,需要列出属性名和对应的值) recursive(设置查找层次,只查找下一层则设置为False)
# string(按照关键字string进行检索,采用string=开始) limit(返回结果的个数,默认返回全部结果)

# 当然也可以获取标签中的属性值
# 可以后续加.<>获取 <>可选: name(标签的名字字符串) attrs(字典,tag所有属性) content(列表,tag下所有子tag内容) string(字符串,tag包含的文本,网页中真实的文字)
# print(soup.p.name)
# print(soup.p.attrs)

# 由于html语法可以在标签内嵌套标签,所以string返回值遵循下列规则:
# 1. 如果标签内没有嵌套其他标签,则返回其中的内容
# 2. 如果标签内部嵌套了其他标签,但是只有一个标签,则返回最里面标签的内容
# 3. 如果标签内部有超过一层嵌套的标签,则返回None

a = soup.find_all('a')  # 查找所有的a标签
print(len(a))
print(soup.find_all('script'))  # 打印所有的script脚本
print(soup.find_all("script", {'src': re.compile('jquery')}))  # 打印符合正则表达式的script
print(soup.find_all(string=re.compile('百度')))  # 将符合正则表达式(含有百度字符)的字串形成一个集合进行输出

# 正则表达式: 字符串的一种逻辑表达,一般在计算机编译器中使用. python中使用正则表达式进行辅助查找 正则表达式是一种规则,只要符合规则就算匹配到 同时也能使用其他扩展符号实现其他功能
