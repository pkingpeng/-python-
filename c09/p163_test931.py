import os
import zipfile

os.chdir('/Users/moqi/Downloads/c09_test/')
zip7file = zipfile.ZipFile('7.zip')
print(zip7file.namelist())

zzz = zip7file.getinfo('7/zzz.txt')
print(zzz.file_size)
print(zzz.compress_size)

print('Compressed file is %sx smaller!' % (round(zzz.file_size / zzz.compress_size, 4)))
zip7file.close()
