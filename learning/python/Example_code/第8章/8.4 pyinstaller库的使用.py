# -*- coding: utf-8 -*-
# @Time : 2020/7/9 5:55
# @Author : MYH
# @File : 8.4 pyinstaller库的使用.py
# @Software: PyCharm

# pyinstaller是一个将Python语言脚本打包成可执行文件的第三方库 可以用于win/mac/linux等操作系统 需要独立安装
# 代码需要在idle / cmd中进行演示

# 使用 pyinstaller <文件路径> 命令即可使用pyinstaller 文件不支持文件名中有点号 .
# 执行完毕后,源文件所在目录将生成dist和build文件夹,其中build是运行过程中的临时文件夹,可以删除的最终打包的程序在dist文件夹中  里面的其他目录是可执行文件的动态链接库
# 使用过程中需要注意的是: 文件路径中不能出现空格和英文点号 文件必须用utf-8编码,暂不支持其他编码格式

# 动态链接库: 动态链接提供了一种方法能够使进程在运行时实际调用不属于其程序的代码 这样可以使代码变得十分精简 windows下提供很多动态链接库的后缀为dll或osx
# 静态链接和动态链接相对,指程序中包含了其所调用的所有代码,这可以让程序在系统间移动而不用考虑函数库是否一致

# pyinstaller有一些参数:
# -h, --help  # 查看帮助
# -v, --version  # 查看版本
# --cleam  # 清理打包过程中的临时文件
# -D, --onedir  # 默认值,生成dist目录
# -F, -onefile  # 在dist文件夹中只生成独立的打包文件
# -p DIR, --paths DIR  # 添加python文件使用的第三方路径
# -i <.ico /.exe /.icns >, --icon <.ico /.exe /.icns >  # 指定打包程序的icon
