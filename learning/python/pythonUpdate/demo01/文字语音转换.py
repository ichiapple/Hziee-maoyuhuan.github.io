# -*- coding: utf-8 -*-
# @Time : 2020/12/1 11:36
# @Author : MYH
# @File : 文字语音转换.py
# @Software: PyCharm
import pyttsx3
from os import path
import speech_recognition as sr


def voiceToText(file_name):
    global content
    print("voiceToText")

    # 语音转文字
    voice_file = path.join(path.dirname(path.realpath(__file__)), file_name)
    # print(voice_file)
    r = sr.Recognizer()
    with sr.AudioFile(voice_file) as source:
        audio = r.record(source)
    try:
        content = r.recognize_google(audio, language='zh-CN')
        # print("Google Speech Recognition:" + content)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Google Speech Recognition error; {0}".format(e))

    return content or '无法翻译'


def textToVoice(note):
    # print("textToVoice")
    engine = pyttsx3.init()
    engine.say(note)
    engine.setProperty('rate', 80)
    engine.setProperty('volume', 0.9)
    engine.runAndWait()
    pass


if __name__ == '__main__':
    while True:
        a = input("请输入数字  语音转文字(0) 或 文字转语音(1) 或 退出(2) :")
        if a == "0":
            voiceToText("sounds\demo01.mp3")
        elif a == "1":
            b = input("请输入要转换的文本:")
            textToVoice(b)
        elif a == "2":
            break
        else:
            print("Input Error!")
