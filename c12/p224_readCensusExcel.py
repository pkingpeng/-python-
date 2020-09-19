#! python3
# Tabulates population and number of census for each county
import pprint

import openpyxl

print('Opening workbook...')

workbook = openpyxl.load_workbook('../resource/excel/censuspopdata.xlsx')
sheet = workbook['Population by Census Tract']

countyData = {}

print('Reading rows...')

for row in range(2, sheet.max_row + 1):
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    countyData.setdefault(state, {})
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

    countyData[state][county]['tracts'] += 1
    countyData[state][county]['pop'] += int(pop)

print('Writing results...')
resultFile = open('../gererate_python_file/census2010.py', 'w')
resultFile.write('allDate = ' + pprint.pformat(countyData))
resultFile.close()

print('Done')
