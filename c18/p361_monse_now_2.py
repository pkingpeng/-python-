#! python3
# mouseNow.py - Displays the mouse cursor's current position.
import pyautogui

"""
复制过来的代码，依然无法正常工作。
不过运行结束时会在当前目录生成一个截图文件，名称类似：
screenshot2020-0414_09-18-44-427623.png
"""

print('Press Ctrl-C to quit.')
try:
    while True:
        # Get and print the mouse coordinates.
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        pixelColor = pyautogui.screenshot().getpixel((x, y))
        positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
        positionStr += ', ' + str(pixelColor[1]).rjust(3)
        positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)

except KeyboardInterrupt:
    print('\nDone.')
