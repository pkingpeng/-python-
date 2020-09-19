import os
import shutil

# 绝对路径
shutil.copy('/Users/moqi/Downloads/c09_test/1/1.txt', '/Users/moqi/Downloads/c09_test/2/1.txt')
# 相对路径
os.chdir('/Users/moqi/Downloads/c09_test/')
shutil.copy('1/zzz.txt', '2/zzz.txt')
# 复制整个文件夹，目标文件夹必须不存在否则报错
shutil.copytree('/Users/moqi/Downloads/c09_test/1/', '/Users/moqi/Downloads/c09_test/2/1_backup')
