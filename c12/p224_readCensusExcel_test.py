from gererate_python_file.census2010 import allDate as data

print(data['AK']['Anchorage'])

anchoragePoe = data['AK']['Anchorage']['pop']
print('The 2010 population of Anchorage was %s.' % anchoragePoe)

"""
{'pop': 291826, 'tracts': 55}
The 2010 population of Anchorage was 291826.
"""
