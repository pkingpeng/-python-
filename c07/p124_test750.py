import re

regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
match = regex.search('Home is 888-888-8888, Office is 999-999-9999')
print(match.group())

all_element = regex.findall('Home is 888-888-8888, Office is 999-999-9999')
print(all_element)

group_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
all_element = group_regex.findall('Home is 888-888-8888, Office is 999-999-9999')
print(all_element)

print(all_element[0][1])

"""
888-888-8888
['888-888-8888', '999-999-9999']
[('888', '888-8888'), ('999', '999-9999')]
888-8888
"""
