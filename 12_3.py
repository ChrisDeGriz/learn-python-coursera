# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def parse_link(link):
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup('a')

url = input('Enter URL:')
count = int(input('Enter count:'))
position = int(input('Enter position:'))

for num in range(count):
    tags = parse_link(url)

    list = []
    for tag in tags:
        list.append(tag.get('href', None))

    url = list[position - 1]

print(url)
