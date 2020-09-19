import json

jsonString = '''{
  "name": "zhangsan",
  "isCat": true,
  "miceCaught": 0
}
'''

data = json.loads(jsonString)
print(data)

"""
{'name': 'zhangsan', 'isCat': True, 'miceCaught': 0}
"""
