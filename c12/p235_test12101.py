"""
"""
import openpyxl

xlsx = '../resource/excel/dimensions.xlsx'

wb = openpyxl.Workbook()
sheet = wb['Sheet']

sheet['A1'] = 'Tall row'
sheet['A2'] = 'Wide column'

sheet.row_dimensions[1].height = 70
sheet.column_dimensions['B'].width = 20

wb.save(xlsx)

print('Generate Success')
