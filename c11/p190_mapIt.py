#! python3
# Launches a map in the browser using an address from the command line or clipboard.

""""
test: copy next line and run this program
870 Valencia St, San Francisco, CA 94110
"""
import sys
import webbrowser

import pyperclip

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
