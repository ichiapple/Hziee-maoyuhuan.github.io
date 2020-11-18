# -*- coding: utf-8 -*-
# @Time : 2020/11/18 18:35
# @Author : MYH
# @File : 找色差.py
# @Software: PyCharm

# !/usr/local/bin/python3.7
import cv2
import numpy as np
from mss import mss
from collections import Counter
from  pynput.mouse import Button, Controller

import time

mouse = Controller()

cords = {'top': 140, 'left': 2090, 'width': 570, 'height': 540}
A = time.time()
while time.time() - A < 61:
    with mss() as sct:
        img = np.array(sct.grab(cords))  # sct.grab(cords/monitor)
    #
    img[img == img[0, -1]] = 0  # remove the boarder
    img[img == img[0, 0]] = 0  # remove the boarder
    img[img == img[10, 10]] = 0  # first bin
    Ra = 6  # rsize to reduce the unnecessary calculates
    # if the first bin is the target
    if np.sum(img[520, 10]) > 0 and np.sum(img[520, 500]) > 0:
        print("First bin")
        # mouse.position = (2090+30, 140+30)
        # mouse.press(Button.left)
        # mouse.release(Button.left)
    else:
        Signal = "Run"
        for i in range(int(540 / Ra) - 5):
            i = i * Ra
            for ii in range(int(570 / Ra) - 10):
                ii = ii * Ra
                if np.sum(img[i, ii]) > 0 and np.sum(img[i, ii] - img[i + 3, ii + 4]) == 0:
                    img[i:i + 4, ii:ii + 4] = 255
                    print(i, ii)
                    # mouse.position = (2090+ii+10, 140+i+10)
                    # mouse.press(Button.left)
                    # mouse.release(Button.left)
                    Signal = "Break"
                    break
            if Signal == "Break":
                break

    cv2.imshow('image', img)
    cv2.moveWindow("image", 2800, 0)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

cv2.destroyAllWindows()