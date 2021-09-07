ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

combinations = ((a, b) for a in ports for b in ports if a < b)
i = 0

for combination in combinations:
    print(combination)
    i += 1
else:
    print(f'Number of connections: {i}')

