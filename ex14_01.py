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

dr_url2 = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
dr_url = "http://www.dr-chuck.com"

url = input('Enter - ')
if len(url) < 1:
    url = dr_url2

count1 = 0

while True:

    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve all of the anchor tags
    tags = soup('a')
    count2 = 0
    numlist = list()
    count1 = count1 + 1
    print('Count1:', count1)

    for tag in tags:
        # Look at the parts of a tag
        tag = str(tag)
        print('TAG:', tag)
        count2 = count2 + 1
        print('Count2:', count2)

        if count2 == 3:
            url = re.findall('^http\S+@\S+',tag)

            print('url:', url)

            break



    if count1 == 3:
        break
