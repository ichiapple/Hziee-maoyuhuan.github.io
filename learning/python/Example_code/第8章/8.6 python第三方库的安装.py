# -*- coding: utf-8 -*-
# @Time : 2020/7/9 19:57
# @Author : MYH
# @File : 8.6 python第三方库的安装.py
# @Software: PyCharm

# python第三方库有三种安装方式:Pip工具安装 自定义安装 文件安装

# pip工具的格式为: pip -command -option 是python第三方库最主要的安装方式 可以安装超过90%的第三方库
# 其中command可以是: install/download/uninstall/freeze/list/show/search/wheel/hash/completion/help 例如: pip install <拟安装包名>
# install选项后还可以跟上 -U 表示update 用于升级库

# 自定义安装: 从第三方库对应的官网上进行下载,根据提示进行安装 通常适用于pip命令无登记或者安装失败的库

# 文件安装: 从网页中获取第三方库安装文件 .whl文件 下载完毕通过pip进行安装
# whl文件是python库的一种打包方式,用于通过pip命令进行安装 相当于python库的安装包文件 本质上是一个压缩格式文件 可以通过修改后缀为.zip查看其内容
# whl格式是用于替代python早期的eggs格式,是python打包格式的事实标准
