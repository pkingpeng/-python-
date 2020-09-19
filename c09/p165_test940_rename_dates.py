#! python3
# Renames filenames with American MM-DD-YYYY date format to European DD-MM-YYYY

"""
test fir: /Users/moqi/Downloads/c09_test/940/
test file:
08-30-2020.txt
11-18-2002sdfsdfsdf.txt
ahusfå7-27-1999sfdsdf.txt
"""
import os
import re
import shutil

# Create a regex that matches files with the American date format

datePattern = re.compile(r"""^(.*?)     # all text before the date
    (([01])?\d)-                        # one or two digits for the month
    (([0123])?\d)-                      # one or two digits for the day
    ((19|20)\d\d)                       # four digits for the year, only start 19 or 20
    (.*?)$                              # all text after the date
    """, re.VERBOSE)

test_dir = '/Users/moqi/Downloads/c09_test/940/'
for americanFileName in os.listdir(test_dir):
    mo = datePattern.search(americanFileName)

    if mo:
        beforePart = mo.group(1)
        monthPart = mo.group(2)
        dayPart = mo.group(4)
        yearPart = mo.group(6)
        afterPart = mo.group(8)

        europeFileName = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
        europeFullFileName = os.path.join(test_dir, europeFileName)
        americanFullFileName = os.path.join(test_dir, americanFileName)

        print('Renaming %s to %s.' % (americanFullFileName, europeFullFileName))
        shutil.move(americanFullFileName, europeFullFileName)

"""
Renaming /Users/moqi/Downloads/c09_test/940/11-18-2002sdfsdfsdf.txt to /Users/moqi/Downloads/c09_test/940/18-11-2002sdfsdfsdf.txt.
Renaming /Users/moqi/Downloads/c09_test/940/ahusfå7-27-1999sfdsdf.txt to /Users/moqi/Downloads/c09_test/940/ahusfå27-7-1999sfdsdf.txt.
Renaming /Users/moqi/Downloads/c09_test/940/08-30-2020.txt to /Users/moqi/Downloads/c09_test/940/30-08-2020.txt.
"""
