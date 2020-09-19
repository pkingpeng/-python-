import datetime

oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))
print(oct21st.strftime('%I:%M %p'))
print(oct21st.strftime('%B of %y'))
"""
2015/10/21 16:29:00
04:29 PM
October of 15
"""
