"""
https://openpyxl.readthedocs.io/en/stable/styles.html
"""
import openpyxl
from openpyxl.styles import Font

wb = openpyxl.Workbook()
sheet = wb['Sheet']

italic24Font = Font(size=24, italic=True)

a1 = sheet.cell(row=1, column=2)
a1.font = italic24Font
a1.value = 'Hello world'

wb.save('../resource/excel/output/styled.xlsx')
print('Done.')
