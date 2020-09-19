import re

regex = re.compile(r'.*')
all_data = regex.findall('Hello \n World')
print(all_data)

regex = re.compile(r'.*', re.DOTALL)
all_data = regex.findall('Hello \n World')
print(all_data)

"""
['Hello ', '', ' World', '']
['Hello \n World', '']
"""
