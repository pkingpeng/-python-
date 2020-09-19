import re

regex = re.compile(r'nobody', re.IGNORECASE)
data = regex.findall('nobody, NOBODY, NoBoDy')
print(data)
"""
['nobody', 'NOBODY', 'NoBoDy']
"""
