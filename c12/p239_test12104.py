"""
https://openpyxl.readthedocs.io/en/stable/charts/introduction.html
"""
import openpyxl
from openpyxl.chart import BarChart, Reference, Series

wb = openpyxl.Workbook()
sheet = wb.active

for i in range(1, 11):
    sheet['A' + str(i)] = i

refObj = Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)
seriesObj = Series(refObj, title='First series')

chatObj = openpyxl.chart.BarChart()
chatObj.append(seriesObj)

sheet.add_chart(chatObj)
wb.save('../resource/excel/sampleChart.xlsx')
print('Done')
