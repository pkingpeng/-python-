import time

print(time.time())


def calcProd():
    product = 1
    for i in range(1, 100000):
        product *= i
    return product


startTime = time.time()
result = calcProd()
endTime = time.time()

print('The result is %s digits long, took %s seconds to calculate.' % (len(str(result)), (endTime - startTime)))

"""
1586680463.075951
The result is 456569 digits long, took 2.2562198638916016 seconds to calculate.
"""
