#! python3
# Copies an entire folder and its contents into a ZIP file whose filename increments

"""
test fir: /Users/moqi/Downloads/c09_test/940/
test file:
08-30-2020.txt
11-18-2002sdfsdfsdf.txt
ahusfå7-27-1999sfdsdf.txt
"""
import os
import zipfile

test_dir = '/Users/moqi/Downloads/c09_test/940/'


def backupToZip(target_dir):
    folder = os.path.abspath(target_dir)
    os.chdir(target_dir)
    number = 1

    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'

        if os.path.exists(zipFilename):
            number += 1
        else:
            break

    print('Creating %s...' % zipFilename)
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    for folderName, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % folderName)
        backupZip.write(folderName)

        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(folder, filename))

    backupZip.close()
    print('Done.')


backupToZip(test_dir)
