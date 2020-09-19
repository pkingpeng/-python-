"""
https://openpyxl.readthedocs.io/en/stable/tutorial.html
"""
import openpyxl

wb = openpyxl.load_workbook('../resource/excel/example.xlsx')
sheet = wb['Sheet1']
print(tuple(sheet['A1':'C3']))

print('\n%s\n' % ('-' * 50))

for rowOfCCellObjects in sheet['A1':'C3']:
    for cellObj in rowOfCCellObjects:
        print(cellObj.coordinate, cellObj.value)
    print('--- End Of Row ---')

print('\n%s\n' % ('-' * 50))

sheet = wb.active
print(sheet['B'])
for cellObj in sheet['B']:
    print(cellObj.value)

"""
((<Cell 'Sheet1'.A1>, <Cell 'Sheet1'.B1>, <Cell 'Sheet1'.C1>), (<Cell 'Sheet1'.A2>, <Cell 'Sheet1'.B2>, <Cell 'Sheet1'.C2>), (<Cell 'Sheet1'.A3>, <Cell 'Sheet1'.B3>, <Cell 'Sheet1'.C3>))

--------------------------------------------------

A1 2015-04-05 13:34:02
B1 Apples
C1 73
--- End Of Row ---
A2 2015-04-05 03:41:23
B2 Cherries
C2 85
--- End Of Row ---
A3 2015-04-06 12:46:51
B3 Pears
C3 14
--- End Of Row ---

--------------------------------------------------

(<Cell 'Sheet1'.B1>, <Cell 'Sheet1'.B2>, <Cell 'Sheet1'.B3>, <Cell 'Sheet1'.B4>, <Cell 'Sheet1'.B5>, <Cell 'Sheet1'.B6>, <Cell 'Sheet1'.B7>)
Apples
Cherries
Pears
Oranges
Apples
Bananas
Strawberries
"""
