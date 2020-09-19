import re

phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
match = phone_num_regex.search('My number is 888-888-8888.')
print('Phone number found: ' + match.group())
"""
Phone number found: 888-888-8888
"""
