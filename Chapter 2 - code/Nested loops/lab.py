ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

combinations = [(a, b) for a in ports for b in ports if a != b]
print(combinations)
print(len(combinations))

combinations = [(a, b) for a in ports for b in ports if a < b]
print(combinations)
print(len(combinations))