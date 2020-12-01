# -*- coding: utf-8 -*-
# @Time : 2020/12/1 11:36
# @Author : MYH
# @File : 文字语音转换.py
# @Software: PyCharm


def voiceToText():
    print("voiceToText")
    pass


def textToVoice():
    print("textToVoice")
    pass


if __name__ == '__main__':
    while True:
        a = input("请输入数字  语音转文字(0) 或 文字转语音(1) 或 退出(2) :")
        if a == "0":
            voiceToText()
        elif a == "1":
            textToVoice()
        elif a == "2":
            break
        else:
            print("Input Error!")
