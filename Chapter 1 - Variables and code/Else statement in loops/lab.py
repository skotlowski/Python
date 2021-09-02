import os
import urllib.request


data_dir = r'C:\repositories\Python\Chapter 1 - Variables and code\Else statement in loops\www'
pages = [{'name': 'mobilo', 'url': 'http://www.mobilo24.eu/'},
         {'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/'},
         {'name': 'kursy', 'url': 'http://www.kursyonline24.eu/'}]

for item in pages:
    webpage_name = list(item.values())[0]
    webpage_url = list(item.values())[1]
    path = fr'{data_dir}\{webpage_name}.html'

    try:
        print(f'Processing {webpage_name}')
        urllib.request.urlretrieve(webpage_url, path)
    except:
        print(f'Failure processing web page {webpage_name}')
        break
else:
    print(f'Web pages downloaded successfully!')
