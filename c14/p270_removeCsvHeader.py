#! python3
# Removes the header from all csv files in the current working directory

import csv
import os

os.chdir('/Users/moqi/Downloads/')
os.makedirs('headerRemoved', exist_ok=True)

for fileName in os.listdir('.'):
    if not fileName.endswith('.csv'):
        continue

    csvFileObj = open(fileName)
    readerObj = csv.reader(csvFileObj)
    data = list(readerObj)
    outCsvFileObj = open(os.path.join('headerRemoved', fileName), 'w')
    writer = csv.writer(outCsvFileObj)

    print('Removing header from %s' % fileName)

    for index in range(1, len(data)):
        writer.writerow(data[index])

    csvFileObj.close()
    outCsvFileObj.close()

print('Done.')
