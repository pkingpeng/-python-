import os

"""
一些不需要的、巨大的文件或文件夹占据了硬盘的空间，这并不少见。
如果你试图释放计算机上的空间，那么删除不想要的巨大文件效果最好。但首先你必须找到它们。

编写一个程序，遍历一个目录树，查找特别大的文件或文件夹，比方说，超过 100MB 的文件
（回忆一下，要获得文件的大小，可以使用 os 模块的 os.path.getsize()）。将这些文件的绝对路径打印到屏幕上。
"""


def printLargeFileName(source_dir):
    print('These files are more than 100MB :\n')
    for folderName, subfolders, filenames in os.walk(source_dir):

        for filename in filenames:
            fileSize = os.path.getsize(os.path.join(folderName, filename))
            # 取出所有大于 100MB 的文件名
            if fileSize > 104857600:
                print('%s, %5.2fMB' % (filename, round(fileSize / 1048576, 4)))

    print('\nDone.')


test_dir = '/Users/moqi/PDF/'
printLargeFileName(test_dir)
