"""
跨模块调用参考这篇文章： https://www.jianshu.com/p/61ed747680e2
"""
from gererate_python_file.my_cat import *

print(cats)
print(cats[0])
print(cats[0]['name'])
"""
[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]
{'desc': 'chubby', 'name': 'Zophie'}
Zophie
"""
