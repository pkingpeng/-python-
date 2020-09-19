#!/usr/local/bin/python3
# check password strong

import re


def check(password):
    if not password:
        return False

    lengthCheck = re.findall(r'(.){9,}', password)
    digitCheck = re.findall(r'[^A-Za-z0-9]+', password)
    UpperCheck = re.findall(r'[A-Z]+', password)
    lowerCheck = re.findall(r'[a-z]+', password)
    numberCheck = re.findall(r'[0-9]+', password)

    print(lengthCheck, digitCheck, UpperCheck, lowerCheck, numberCheck)

    if lengthCheck and not digitCheck and UpperCheck and lowerCheck and numberCheck:
        return True
    else:
        return False


print(check('99999999'))
print(check('123'))
print(check('abcdabcdE'))
print(check('AbcdAbcdE'))
print(check('&&&AbcdAbcdE'))
print(check('AbcdAbcdE1'))
print(check('ABCDABCDE1'))

"""
[] [] [] [] ['99999999']
False
[] [] [] [] ['123']
False
['E'] [] ['E'] ['abcdabcd'] []
False
['E'] [] ['A', 'A', 'E'] ['bcd', 'bcd'] []
False
['E'] ['&&&'] ['A', 'A', 'E'] ['bcd', 'bcd'] []
False
['1'] [] ['A', 'A', 'E'] ['bcd', 'bcd'] ['1']
True
['1'] [] ['ABCDABCDE'] [] ['1']
False
"""
