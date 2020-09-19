import json

pythonValueDic = {
    'name': 'zhangsan',
    'isCat': True,
    'miceCaught': 0
}

data = json.dumps(pythonValueDic)
print(data)

"""
{"name": "zhangsan", "isCat": true, "miceCaught": 0}
"""
