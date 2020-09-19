#! python3
# Automatically fills in the form.

"""
测试问卷地址 https://wj.qq.com/s2/5876762/a132/
"""

import time

import pyautogui

from c17.c17_image_constant import *

nameField = (619, 775)
genderField = (663, 911)
pyautogui.PAUSE = 0.5

print('>>> 切屏到 Chrome <<<')
# 腾讯问卷提交图标
submitPng = image_path + 'tencent_submit.png'

formData = []
for i in range(100):
    formData.append({'name': 'zhangsan' + str(i), 'gender': 'man' if i % 2 == 0 else 'woman'})

for person in formData:
    print('>>> 1 Second pause to let user press ctrl-c <<<')
    time.sleep(1)

    screenBox = pyautogui.locateOnScreen(submitPng)
    while not screenBox:
        print('Wait until the form page has loaded.')
        time.sleep(0.5)

    print('Entering %s info...' % person['name'])

    pyautogui.click(nameField[0], nameField[1])
    pyautogui.typewrite(person['name'])
    pyautogui.click(genderField[0], genderField[1])
    pyautogui.typewrite(person['gender'])

    print('Click submit.')
    submitIndex = pyautogui.center(screenBox)
    (x, y) = submitIndex
    print(submitIndex)
    x, y = x // 2, y // 2
    print('x = %d, y = %d' % (x, y))
    pyautogui.click(x, y)

    print('Refresh page')
    time.sleep(1)
    pyautogui.hotkey('command', 'r')
