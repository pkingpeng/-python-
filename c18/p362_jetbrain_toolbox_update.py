from c18.c18_click import click_by_list

"""
自动点击 JetBrian ToolBox 的更新。
要求 JetBrain ToolBox 处于坐标位置。
"""
click_list = [
    ('jetbrain toolbox icon', (1314, 11)),
    ('top right setting button', (1500, 52)),
    ('check for updates', (1383, 145)),
    ('projects/tools to return main interface', (1131, 56)),
]

click_by_list(click_list, 1)
