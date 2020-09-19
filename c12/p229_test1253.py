import openpyxl

wb = openpyxl.Workbook()
print(wb.sheetnames)

sheet = wb.active
sheet['A1'] = 'Hello World!!!'
print(sheet['A1'].value)

"""
['Sheet']
Hello World!!!
"""
