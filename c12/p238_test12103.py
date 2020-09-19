"""
"""
import openpyxl

wb = openpyxl.load_workbook('../resource/excel/produceSales.xlsx')
sheet = wb['Sheet']
sheet.freeze_panes = 'A2'
wb.save('../resource/excel/freezeExample.xlsx')

print('Done')
