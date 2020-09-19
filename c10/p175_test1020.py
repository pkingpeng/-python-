def spam():
    bacon()


def bacon():
    raise Exception('This is the error message')


spam()
"""
Traceback (most recent call last):
  File "/Users/moqi/Documents/Code/automate-the-boring-stuff/c10/p175_test1020.py", line 7, in <module>
    spam()
  File "/Users/moqi/Documents/Code/automate-the-boring-stuff/c10/p175_test1020.py", line 2, in spam
    bacon()
  File "/Users/moqi/Documents/Code/automate-the-boring-stuff/c10/p175_test1020.py", line 5, in bacon
    raise Exception('This is the error message')
Exception: This is the error message
"""
