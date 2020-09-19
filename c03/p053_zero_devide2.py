def spam(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        print('Error: Invalid argument')


print(spam(0))

"""
Error: Invalid argument
None
"""
