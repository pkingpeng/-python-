import datetime

print(datetime.datetime.strptime('October 21, 2018', '%B %d, %Y'))
print(datetime.datetime.strptime('2018/10/21 12:33:44', '%Y/%m/%d %H:%M:%S'))
print(datetime.datetime.strptime('October of 15', '%B of %y'))
print(datetime.datetime.strptime('November of 63', '%B of %y'))

"""
2018-10-21 00:00:00
2018-10-21 12:33:44
2015-10-01 00:00:00
2063-11-01 00:00:00
"""
