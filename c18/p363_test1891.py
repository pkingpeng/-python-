import pyautogui

"""
Hello worldHello worldHello world
XYabXYabXyab
print("hello world")!!!print("hello world")!print("hello world")!!!!!
&&&





"""

# 运行时请将 4-7 行删除，以便展示效果
pyautogui.click(558, 153)
pyautogui.typewrite('Hello world')

pyautogui.click(558, 179)
pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'])

pyautogui.click(558, 200)
pyautogui.typewrite('print("hello world")!!!')

pyautogui.click(558, 226)
pyautogui.keyDown('shift')
pyautogui.press('7')
pyautogui.keyUp('shift')

pyautogui.click(558, 271)
# pyautogui.hotkey('command', 'a')
# pyautogui.hotkey('command', 'c')
# pyautogui.hotkey('command', 'v')
# pyautogui.hotkey('command', 'z')

