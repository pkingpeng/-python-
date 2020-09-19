import pyautogui

im = pyautogui.screenshot()

print(im.getpixel((0, 0)))
print(im.getpixel((50, 200)))

print(pyautogui.pixelMatchesColor(50, 200, (240, 240, 240, 255)))
print(pyautogui.pixelMatchesColor(50, 200, (100, 100, 240, 255)))

"""
(205, 227, 242, 255)
(240, 240, 240, 255)
True
False
"""
