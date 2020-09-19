import re

regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
match = regex.search('My number is 888-888-8888.')

print(match.group(1))
print(match.group(2))
print(match.group(0))
print(match.group())

area_code, main_number = match.group(1), match.group(2)
print(area_code)
print(main_number)
