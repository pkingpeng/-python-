import pyautogui

# 移动到指定位置
pyautogui.moveTo(1000, 500, duration=2)


# 滚动鼠标
print('滚动鼠标：')
for i in range(1000):
    pyautogui.scroll(1)
