#!/usr/local/bin/python3
"""
mcb.pyw - Saves and loads pieces of text to the clipboard.
Usage: python3 mcb.pyw save <keyword> - Saves clipboard to keyword.
       python3 mcb.pyw <keyword> - Loads keyword to clipboard.
       python3 mcb.pyw list - Loads all keywords to clipboard.
"""

import shelve
import sys

import pyperclip

mcbShelf = shelve.open('../resource/binary/mcb')
parameters = sys.argv
print(parameters)

if len(parameters) == 3 and parameters[1].lower() == 'save':
    mcbShelf[parameters[2]] = pyperclip.paste()
elif len(parameters) == 2:
    if parameters[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif parameters[1] in mcbShelf:
        pyperclip.copy(mcbShelf[parameters[1]])

mcbShelf.close()
