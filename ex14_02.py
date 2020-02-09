# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
import urllib.request, urllib.parse, urllib.error

from bs4 import BeautifulSoup
import ssl

import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

a_url = "http://py4e-data.dr-chuck.net/known_by_Eren.html"
s_url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"


url = input('Enter - ')
end_count = input('Enter count : ')
end_position = input('Enter position : ')

if len(url) < 1:
    url = a_url

count = 0

while True:

    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve all of the anchor tags
    tags = soup('a')
    position = 0
    numlist = list()
    count = count + 1
#    print('count:', count)

    for tag in tags:
        # Look at the parts of a tag
        tag = tag.get('href', None)

        position = position + 1
#        print('position:', position)

        if position == int(end_position):
            url = tag
            print('url:', url)
            print("")

            break

    if count == int(end_count):
        break
