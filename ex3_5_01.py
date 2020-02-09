
import urllib.request, urllib.parse, urllib.error

import xml.etree.ElementTree as ET

# url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

url = 'http://py4e-data.dr-chuck.net/comments_238927.xml'

url_open = urllib.request.urlopen(url)

data = url_open.read()
print('Retrieved', len(data), 'characters')
print(data.decode())

tree = ET.fromstring(data)

print('############################')

print('tree:',tree)

print('############################')

list = tree.findall('.//count')
print('count', len(list))

sum = 0
for item in list:
#    print( item.tag, item.text)
    count = int(item.text)
    sum = sum + count

    print('sum:', sum)
