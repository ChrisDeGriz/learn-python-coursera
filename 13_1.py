import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL:')
xml = urllib.request.urlopen(url, context=ctx).read()

data = ET.fromstring(xml)

comments = data.findall('comments/comment')

sum = 0
count = len(comments)

for comment in comments:
    sum = sum + int(comment.find('count').text)

print('Count:', count)
print('Sum:', sum)
