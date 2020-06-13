import json
import ssl
from urllib.request import urlopen

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
data = urlopen(url, context=ctx).read().decode()
print(data)
info = json.loads(data)
print('User count:', len(info['comments']))

aCsum = 0
for item in info['comments']:
    aCsum += int(item['count'])
print(aCsum)    
