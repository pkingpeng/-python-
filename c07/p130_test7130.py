import re

regex1 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
regex2 = re.compile(r'''
                        (\d\d\d)    # area code
                        -
                        (\d\d\d-\d\d\d\d)   # main number
                        ''', re.VERBOSE)

match1 = regex1.search('My number is 888-888-8888.')
print(match1)
match2 = regex2.search('My number is 888-888-8888.')
print(match2)
"""
<re.Match object; span=(13, 25), match='888-888-8888'>
<re.Match object; span=(13, 25), match='888-888-8888'>
"""
