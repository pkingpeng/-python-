import csv

outputFile = open('../resource/csv/output/output.csv', 'w')
writer = csv.writer(outputFile)

writer.writerow(['spam', 'eggs', 'bacon', 'ham'])
writer.writerow(['Hello world', 'eggs', 'bacon', 'ham'])
writer.writerow([1, 2, 3.1415926, 4])

outputFile.close()
print('Done.')
