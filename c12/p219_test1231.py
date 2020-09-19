import openpyxl

wb = openpyxl.load_workbook('../resource/excel/example.xlsx')
print(type(wb))
"""
<class 'openpyxl.workbook.workbook.Workbook'>
"""
