import datetime

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())

dt = datetime.datetime.now()
print(dt)
thousandDays = datetime.timedelta(days=1000)
# 在 Print 里天数增加了 1000，👍
print(dt + thousandDays)

oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
aboutThirtyYears = datetime.timedelta(days=365 * 30)
print(oct21st)
print(oct21st - aboutThirtyYears)
print(oct21st - (2 * aboutThirtyYears))

"""
11 36548 0
986948.0
11 36548 0
986948.0
2020-04-12 16:57:29.170100
2023-01-07 16:57:29.170100
2015-10-21 16:29:00
1985-10-28 16:29:00
1955-11-05 16:29:00
"""
