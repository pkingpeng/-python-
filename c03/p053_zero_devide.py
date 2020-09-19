def spam(divide_by):
    return 42 / divide_by


print(spam(0))

"""
Traceback (most recent call last):
  File "/Users/moqi/Documents/Code/automate-the-boring-stuff/c03/p053_zero_devide.py", line 5, in <module>
    print(spam(0))
  File "/Users/moqi/Documents/Code/automate-the-boring-stuff/c03/p053_zero_devide.py", line 2, in spam
    return 42 / divide_by
ZeroDivisionError: division by zero
"""
