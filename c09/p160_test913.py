import os

# 删除 /Users/moqi/Downloads/c09_test/9/ 下所有的 txt 文件，不会递归删除
os.chdir('/Users/moqi/Downloads/c09_test/9/')
for filename in os.listdir():
    if filename.endswith('.txt'):
        print('These file will be delete: %s.' % filename)
        os.unlink(filename)
