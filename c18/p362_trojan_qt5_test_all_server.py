import pyautogui

from c18.c18_click import click_by_list

"""
自动点击 Trojan Qt5 的测试节点速度。
"""
click_list = [
    ('hidden bar icon', (1227, 12)),
    ('trojan qt5 icon', (1030, 15)),
    ('restore button', (1104, 208)),
    ('connection button', (802, 265)),
    ('Test All Connections Latency button', (870, 465))
]


click_by_list(click_list, 0.25)

# 全屏显示 Trojan Qt5
# pyautogui.hotkey('control', 'option', 'command', 'm')

# click_by_list(click_list2, 3)
