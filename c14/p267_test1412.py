import csv

exampleFile = open('../resource/csv/example.csv')
reader = csv.reader(exampleFile)

for row in reader:
    print('Row #%d is %s' % (reader.line_num, row))

"""
Row #1 is ['4/5/2014 13:34', 'Apples', '73']
Row #2 is ['4/5/2014 3:41', 'Cherries', '85']
Row #3 is ['4/6/2014 12:46', 'Pears', '14']
Row #4 is ['4/8/2014 8:59', 'Oranges', '52']
Row #5 is ['4/10/2014 2:07', 'Apples', '152']
Row #6 is ['4/10/2014 18:10', 'Bananas', '23']
Row #7 is ['4/10/2014 2:40', 'Strawberries', '98']
"""
