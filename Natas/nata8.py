import requests
import re
import base64

username = 'natas8'
password = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'
url = 'http://%s.natas.labs.overthewire.org/index-source.html' % username
res = requests.get(url, auth=(username, password))
hashsecret = '3d3d516343746d4d6d6c315669563362'
decodehex = bytes.fromhex(hashsecret).decode()
revstr = decodehex[::-1]
decodebase64 = re.findall("b'(.*)'",str(base64.b64decode(revstr)))[0]
print(decodebase64)
url = 'http://%s.natas.labs.overthewire.org/' % username
session = requests.Session()
res = session.post(url, data={"secret": decodebase64, "submit": "submit"}, auth=(username, password))
content = res.text
print(re.findall("natas9 is (.*)",content)[0])
