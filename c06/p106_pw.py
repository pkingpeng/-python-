#!/usr/local/bin/python3
# An inseure password locker program.
import sys

import pyperclip

passwords = {
    'email': 'hello@gmail.com',
    'blog': 'vvvvv',
    'luggage': '123456'
}

if len(sys.argv) < 2:
    print('Usage: python3 p106_pw.py [account] - copy account password')
    sys.exit()
else:
    account = sys.argv[1]  # first command line arg is the account name

    if account in passwords:
        pyperclip.copy(passwords[account])
        print('Password for ' + account + ' copied to clipboard.')
    else:
        print('There is no account named ' + account)

"""
-> % python3 p106_pw.py email
Password for email copied to clipboard.

-> % python3 p106_pw.py blog 
Password for blog copied to clipboard.
"""
