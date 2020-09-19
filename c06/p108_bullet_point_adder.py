#!/usr/local/bin/python3
# Adds Wikipedia bullet points to the start of each line of text on the clipboard.
# Fist step is copy something, like line 6 to line 9

"""
Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars
"""
from pprint import pprint

import pyperclip

text = pyperclip.paste()

pprint(text)

lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)
pprint(text)

pyperclip.copy(text)

"""
('Lists of animals\n'
 'Lists of aquarium life\n'
 'Lists of biologists by author abbreviation\n'
 'Lists of cultivars')
('* Lists of animals\n'
 '* Lists of aquarium life\n'
 '* Lists of biologists by author abbreviation\n'
 '* Lists of cultivars')
"""
