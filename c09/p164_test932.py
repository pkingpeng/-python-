import os
import zipfile

os.chdir('/Users/moqi/Downloads/c09_test/')

zip7file = zipfile.ZipFile('7.zip')
# 全部解压
zip7file.extractall()
# 单个解压
zip7file.extract('7/zzz.txt')
# 单个解压到其他地方
zip7file.extract('7/zzz.txt', '/Users/moqi/Downloads')

zip7file.close()
