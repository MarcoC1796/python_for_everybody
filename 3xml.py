from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
input = urlopen(url, context=ctx).read()

stuff = ET.fromstring(input)
lst = stuff.findall('.//count')
print('Count count: ', len(lst))

aCsum = 0
for item in lst:
    aCsum += int(item.text)
print(aCsum)
