
import urllib.request, urllib.parse, urllib.error
import json


#while True:
address = input('Enter json url: ')
if len(address) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_238928.json'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode('utf-8')
print('Retrieved', len(data), 'characters')
#print('data:', data)

try:
    js = json.loads(data)
except:
    js = None

print('js :', len(js))
sum = 0
for item in js:
    if item == 'comments':
        for it in js['comments']:
            count = it['count']
            count = int(count)
            sum = sum + count
            print ('count:', count, 'sum:', sum)
