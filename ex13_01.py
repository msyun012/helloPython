# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
# http://www.dr-chuck.com

from urllib.request import urlopen
import urllib.request, urllib.parse, urllib.error

from bs4 import BeautifulSoup
import ssl

import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

dr_url2 = "http://py4e-data.dr-chuck.net/comments_238925.html"
dr_url = "http://www.dr-chuck.com"

url = input('Enter - ')
if len(url) < 1:
    url = dr_url2

html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('tr')
count = 0
numlist = list()

for tag in tags:
    # Look at the parts of a tag
    tag = str(tag)
    print('TAG:', tag)
    number = re.findall('[0-9]+',tag)
    for num in number:
        n = int(num)
        numlist.append(n)

print('Sum:', sum(numlist) )
print("Count:", len(numlist))
