import os
import re
import sys

"""
正则表达式查找

编写一个程序，打开文件夹中所有的.txt 文件，查找匹配用户提供的正则表达 式的所有行。结果应该打印到屏幕上。
"""

dir_path = input("Enter the dir path: ")

if not os.path.exists(dir_path) and not os.path.isdir(dir_path):
    print('Sorry, the path: %s is not exist or it is not dir path' % dir_path)
    sys.exit(0)

while True:
    input_regex = input('Enter the regex: ')
    try:
        re.compile(input_regex)
        break
    except re.error:
        print('Sorry, the regex is wrong, please check and try again.')

pattern = re.compile(input_regex)

for filename in os.listdir(dir_path):
    full_file_path = dir_path + os.path.sep + filename

    if os.path.isfile(full_file_path) and filename.endswith('.txt'):
        print('\nThis file match %s\nThese lines match: \n' % full_file_path)

        for line in open(full_file_path):
            if pattern.search(line):
                print(line.replace('\n', ''))
