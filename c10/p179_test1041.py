import logging
# 这个导入避免每次使用 logging.debug 调用
from logging import debug

# disable 可以关闭 CRITICAL 级别以下的日志打印
# logging.disable(logging.CRITICAL)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
debug('Start of progrma')


def factorial(n):
    debug('Start of factorial(%s)' % n)
    total = 1

    for i in range(n + 1):
        total *= i
        debug('i is %s, total is %s' % (i, total))

    debug('End of factorial(%s)' % n)
    return total


print(factorial(5))
debug('End of program')
"""
0
2020-04-06 18:40:17,141 - DEBUG - Start of progrma
2020-04-06 18:40:17,142 - DEBUG - Start of factorial(5)
2020-04-06 18:40:17,142 - DEBUG - i is 0, total is 0
2020-04-06 18:40:17,142 - DEBUG - i is 1, total is 0
2020-04-06 18:40:17,142 - DEBUG - i is 2, total is 0
2020-04-06 18:40:17,142 - DEBUG - i is 3, total is 0
2020-04-06 18:40:17,142 - DEBUG - i is 4, total is 0
2020-04-06 18:40:17,142 - DEBUG - i is 5, total is 0
2020-04-06 18:40:17,142 - DEBUG - End of factorial(5)
2020-04-06 18:40:17,142 - DEBUG - End of program
"""
