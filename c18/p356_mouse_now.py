#! python3
# Displays the mouse cursor's current position
import pyautogui

print('Press Command + F12 to quit.')

try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print("All done.")

"""
书中代码在这里不能正常工作，后面再研究。
"""
