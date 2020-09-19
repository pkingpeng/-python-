import pyautogui

from c17.c17_image_constant import *

# submit.png 选用 mac 默认 Wi-Fi 图标
# 似乎没有测试出来点击的效果
submitPng = image_path + 'submit.png'
print(pyautogui.locateOnScreen(submitPng))
print(list(pyautogui.locateAllOnScreen(submitPng)))

print(pyautogui.center(pyautogui.locateOnScreen(submitPng)))
print(pyautogui.click(pyautogui.center(pyautogui.locateOnScreen(submitPng))))
# 给坐标横纵坐标都除 2，刚好可以点击
print(pyautogui.click((1396, 11)))

"""
Box(left=2762, top=0, width=60, height=44)
[Box(left=2762, top=0, width=60, height=44)]
Point(x=2792, y=22)
None
"""
