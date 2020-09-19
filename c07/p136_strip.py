#!/usr/local/bin/python3
# like str strip() function

import re


def like_strip(data, replaceChar=' '):
    if not data:
        return data

    # 这里正则的小括号必须使用非贪婪模式，否则在某些情况下清除后半段的部分
    if replaceChar == ' ':
        return re.sub(r'^\s*(.*?)\s*$', r'\1', data)
    else:
        return re.sub(r'^[' + replaceChar + ']*(.*?)[' + replaceChar + ']*$', r'\1', data)


print(like_strip(""))
print(like_strip(" hello world "))
print(like_strip("---^ hello world ^---", '-'))
print(like_strip("---^ hello world ^---", '-^'))
print(like_strip("---^ hello world ^---", '-^ '))

"""

hello world
^ hello world ^
 hello world 
hello world
"""
