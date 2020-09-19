import os
import shutil

"""
选择性拷贝: 
编写一个程序，遍历一个目录树，查找特定扩展名的文件（诸如.pdf 或.jpg）。
不论这些文件的位置在哪里，将它们拷贝到一个新的文件夹中。

考虑到最细粒度文件名可能重复，所以在新文件夹文件名为旧文件夹路径 + 文件名，使其唯一。
"""


def selectedCopy(source_dir, suffix, target_dir):
    print('Start Copy\n')
    for folderName, subfolders, filenames in os.walk(source_dir):

        for filename in filenames:
            if filename.endswith('.' + suffix):
                sourceFullFileName = os.path.join(folderName, filename)
                targetFileName = sourceFullFileName.replace(source_dir, '').replace(os.path.sep, '_')
                targetFullFileName = os.path.join(target_dir, targetFileName)

                print('Copy %s to %s' % (sourceFullFileName, targetFullFileName))
                shutil.copy(sourceFullFileName, targetFullFileName)

    print('\nDone.')


test_dir = '/Users/moqi/Downloads/c09_test/'
select_suffix = 'txt'
save_dir = '/Users/moqi/Downloads/c09_test/p171_copy_dir'
selectedCopy(test_dir, select_suffix, save_dir)
