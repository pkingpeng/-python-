import os
import zipfile

os.chdir('/Users/moqi/Downloads/c09_test/')

newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('8', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
