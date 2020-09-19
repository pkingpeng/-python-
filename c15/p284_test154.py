import datetime

d = datetime.datetime
now = d.now()
print(now)
print(now.year, now.month, now.day, now.hour, now.minute, now.second)

halloween2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
newyear2016 = datetime.datetime(2016, 1, 1, 0, 0, 0)
oct31_2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)

print(halloween2015 == oct31_2015)
print(halloween2015 > newyear2016)
print(newyear2016 > halloween2015)
print(newyear2016 != oct31_2015)

"""
2020-04-12 16:51:09.666937
2020 4 12 16 51 9
True
False
True
True
"""
