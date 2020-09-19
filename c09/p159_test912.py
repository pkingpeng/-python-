import shutil

# 移动单个文件，如果目标文件夹存在则被覆盖
shutil.move('/Users/moqi/Downloads/c09_test/1/1.txt', '/Users/moqi/Downloads/c09_test/2/')
# 移动单个文件并重命名
shutil.move('/Users/moqi/Downloads/c09_test/1/zzz.txt', '/Users/moqi/Downloads/c09_test/2/zzz2.txt')
# 注意：移动单个文件，目标文件夹不存在，则重命名文件为 3
shutil.move('/Users/moqi/Downloads/c09_test/1/2.txt', '/Users/moqi/Downloads/c09_test/3')
# 注意：目标文件夹中间路径不存在，则会直接报错
shutil.move('/Users/moqi/Downloads/c09_test/1/3.txt', '/Users/moqi/Downloads/9999999999999/3')
