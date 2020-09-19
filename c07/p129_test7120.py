import re

regex = re.compile(r'Agent (\w)\w*')
data = regex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(data)
"""
A**** told C**** that E**** knew B**** was a double agent.
"""
