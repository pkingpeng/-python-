import openpyxl

wb = openpyxl.load_workbook('../resource/excel/example.xlsx')
print(wb.sheetnames)

sheet = wb['Sheet3']
print(sheet)
print(type(sheet))
print(sheet.title)

"""
['Sheet1', 'Sheet2', 'Sheet3']
<Worksheet "Sheet3">
<class 'openpyxl.worksheet.worksheet.Worksheet'>
Sheet3
"""
