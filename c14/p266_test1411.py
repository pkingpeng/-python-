import csv
import pprint

exampleFile = open('../resource/csv/example.csv')
reader = csv.reader(exampleFile)
data = list(reader)

pprint.pprint(data)

print(data[0][0])
print(data[0][1])
print(data[0][2])
print(data[1][1])
print(data[6][1])

"""
[['4/5/2014 13:34', 'Apples', '73'],
 ['4/5/2014 3:41', 'Cherries', '85'],
 ['4/6/2014 12:46', 'Pears', '14'],
 ['4/8/2014 8:59', 'Oranges', '52'],
 ['4/10/2014 2:07', 'Apples', '152'],
 ['4/10/2014 18:10', 'Bananas', '23'],
 ['4/10/2014 2:40', 'Strawberries', '98']]
4/5/2014 13:34
Apples
73
Cherries
Strawberries
"""
