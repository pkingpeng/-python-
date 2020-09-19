""""
python3 -O p176_test1031.py
在运行 Python 时传入-O 选项，可以禁用断言。
"""

market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}


def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'

    assert 'red' in stoplight.values(), 'Neither light is red %s' % stoplight


switchLights(market_2nd)

"""
Traceback (most recent call last):
  File "/Users/moqi/Documents/Code/automate-the-boring-stuff/c10/p176_test1031.py", line 17, in <module>
    switchLights(market_2nd)
  File "/Users/moqi/Documents/Code/automate-the-boring-stuff/c10/p176_test1031.py", line 14, in switchLights
    assert 'red' in stoplight.values(), 'Neither light is red %s' % stoplight
AssertionError: Neither light is red {'ns': 'yellow', 'ew': 'green'}
"""
