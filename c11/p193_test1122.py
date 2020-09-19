import requests

# 请求一个不存在的网页
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
# 直接调用会打印 Traceback 错误
res.raise_for_status()

try:
    res.raise_for_status()
except Exception as error:
    print('These was a problem: %s.' % error)

"""
These was a problem: 404 Client Error: Not Found for url: http://inventwithpython.com/page_that_does_not_exist.
"""
