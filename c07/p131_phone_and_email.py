#!/usr/local/bin/python3
# Finds phone numbers and email addresses on the clipboard

"""
Fake US Telephone Numbers, United States
Local (US)
202-555-0100
202-555-0175
202-555-0100
202-555-0168
202-555-0119
202-555-0153
akshay.khaleed@aallaa.org
gurev@enhancingworkforceleadership.com
"""

import re

import pyperclip

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code     
    (\s|-|\.)?                      # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''', re.VERBOSE)

# Create email regex.

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   # username
    @                   # @ symbol
    [a-zA-Z0-9.-]+      # domain name
    (\.[a-zA-Z]{2,4})   # dot-something
    )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []

for group in phoneRegex.findall(text):
    phoneNum = '-'.join([group[1], group[3], group[5]])
    extension = group[8]

    if extension:
        phoneNum += ' x' + extension
    matches.append(phoneNum)

for group in emailRegex.findall(text):
    matches.append(group[0])

if matches:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

"""
Copied to clipboard: 
202-555-0100
202-555-0175
202-555-0100
202-555-0168
202-555-0119
202-555-0153
akshay.khaleed@aallaa.org
gurev@enhancingworkforceleadership.com
"""
