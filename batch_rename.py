"""
去掉所有 mp4 文件前五个字符
"""

import os

dir1 = '/Users/moqi/Downloads/test_dir/'
os.chdir(dir1)
for filename in os.listdir():
    if filename.endswith('.mp4'):
        print('These file will be rename: %s' % filename)
        print(filename[5:])
        os.rename(dir1 + filename, dir1 + filename[5:])
