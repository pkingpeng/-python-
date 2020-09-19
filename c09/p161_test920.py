import os

#  使用 os.walk 遍历文件夹
for folderName, subFolders, filenames in os.walk('/Users/moqi/Downloads/c09_test/'):
    print('The current folder is %s.' % folderName)

    for subFolder in subFolders:
        print('Subfolder of %s : %s' % (folderName, subFolder))

    for filename in filenames:
        print('File inside %s : %s.' % (folderName, filename))

"""
The current folder is /Users/moqi/Downloads/c09_test/.
Subfolder of /Users/moqi/Downloads/c09_test/ : 9
Subfolder of /Users/moqi/Downloads/c09_test/ : 1
Subfolder of /Users/moqi/Downloads/c09_test/ : 8
Subfolder of /Users/moqi/Downloads/c09_test/ : 2
File inside /Users/moqi/Downloads/c09_test/ : .DS_Store.
The current folder is /Users/moqi/Downloads/c09_test/9.
Subfolder of /Users/moqi/Downloads/c09_test/9 : 1
File inside /Users/moqi/Downloads/c09_test/9 : .DS_Store.
The current folder is /Users/moqi/Downloads/c09_test/9/1.
File inside /Users/moqi/Downloads/c09_test/9/1 : .DS_Store.
File inside /Users/moqi/Downloads/c09_test/9/1 : 3.txt.
File inside /Users/moqi/Downloads/c09_test/9/1 : 2.txt.
File inside /Users/moqi/Downloads/c09_test/9/1 : zzz.txt.
The current folder is /Users/moqi/Downloads/c09_test/1.
File inside /Users/moqi/Downloads/c09_test/1 : .DS_Store.
File inside /Users/moqi/Downloads/c09_test/1 : 3.txt.
File inside /Users/moqi/Downloads/c09_test/1 : 2.txt.
File inside /Users/moqi/Downloads/c09_test/1 : 1.txt.
File inside /Users/moqi/Downloads/c09_test/1 : zzz.txt.
The current folder is /Users/moqi/Downloads/c09_test/8.
File inside /Users/moqi/Downloads/c09_test/8 : .DS_Store.
The current folder is /Users/moqi/Downloads/c09_test/2.
File inside /Users/moqi/Downloads/c09_test/2 : .DS_Store.
File inside /Users/moqi/Downloads/c09_test/2 : 1.txt.

"""
