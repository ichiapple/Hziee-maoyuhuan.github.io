# -*- coding: utf-8 -*-
# @Time : 2020/7/12 0:36
# @Author : MYH
# @File : 10.2 request库的使用.py
# @Software: PyCharm

# 概述request库
# request库是一个简洁并简单处理http请求的第三方库 其最大优点是成功内需编写过程中更接近正常URL的访问过程 本库建立在python的urllib3库基础上,再进行封装功能
# request库支持非常丰富的链接访问功能,包括国际域名和URL获取,http长链接和连接缓存,http会话和cookie保持,浏览器使用风格的SSL验证,基本的摘要认证,有效的键值对Cookie记录,自动解压缩,自动内容解码,文件分块上传,Http(s)代理,连接超时处理,数据流下载等功能
# 更多介绍可以访问: http://docs.python-requests.org

# 导入部分
import requests
import bs4


# request 库解析 网络爬虫和信息提交只是request库能支持的基本功能 与网页请求相关的函数
# requests.get(url[, timeout=n])  # 对应http请求方式的get请求,获取网页的最基本方法, 可以设置超时时间(单位:s)
# requests.post(url, data={'key': value})  # 对应http请求方式的post请求 字典用于传输用户数据
# requests.delete(url)  # 对应http请求方式的delete请求
# requests.head(url)  # 对应http请求方式的head请求
# requests.options(url)  # 对应http请求方式的option请求
# requests.put(url, data={'key': value})  # 对应http请求方式的put请求 字典用于传输用户数据

# r = requests.get("http://www.baidu.com")
# print(r, type(r))  # 直接打印r是请求响应类型代码 类被是response

# response对象的属性
# status_code  # http请求返回的状态代码
# text  # http相应内容的字符串形式
# encoding  # http相应内容的编码方式
# content  # http相应内容的二进制方式

# print(r.status_code, r.encoding)
# print(r.text)
# print(r.content)
# r.encoding = 'utf-8'  # 默认编码是ISO-8859-1 所以中文乱码 这里更改为utf-8
# print(r.text)

# response的方法
# json()  # 如果http包含了json内容则该方法解析json数据
# raise_for_status()  # 如果不是200(成功)则产生异常 可以使用try-except 进行包裹

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 如果不是200则产生异常
        r.encoding = 'utf-8'  # 设置编码格式为utf-8
        return r.text
    except:
        return ""


url = "http://www.baidu.com"  # 通过这个url可以获取到内容则会把内容进行打印
# url = "http://www.111baidu.com"  # 通过这个网址访问不到内容,则会输出一个空串
print(getHTMLText(url))

# http协议中的get和post: http协议中定义了客户端和服务器交互的不同方法,最基本的就是get和post
# get可以根据某一个链接发送或者获得内容,post则用于发送内容
# 区别: get方式可以通过url进行传递数据,待提交的数据是url的一部分,明文可见不安全,提交的数据不可以超过1024字节 post方式则将数据放置在html_header中,密文传输较为安全,理论上长度没有限制
