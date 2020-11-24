# -*- coding: utf-8 -*-
# @Time : 2020/11/24 13:21
# @Author : MYH
# @File : Demo02.py
# @Software: PyCharm


import qrcode
import os
import time
import zxing


def createQRCode():
    # print("create.")
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )
    data = input("请输入文本以生成二维码:")
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    img.save('QRCode.png')
    print("二维码已经生成")
    time.sleep(5)
    pass


def analyzeQRCode(fileName):
    zx = zxing.BarCodeReader()
    zxData = zx.decode(fileName)
    if zxData:
        # print(zxData)
        a = zxData.__getattribute__("raw")
        print(a)
    else:
        print("none")
    pass


while True:
    a = input("输入 解析(0) 或者 生成(1):")
    if a == '1':
        createQRCode()
        break
    elif a == '0':
        fileName = '\\barcode.jpg'
        print(os.getcwd() + fileName)
        analyzeQRCode(os.getcwd() + fileName)
        break
    else:
        print("输入错误")
