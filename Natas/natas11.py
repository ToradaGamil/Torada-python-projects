import requests
import re
username = 'natas11'
password = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'
url = 'http://%s.natas.labs.overthewire.org/index-source.html' % username
sess = requests.Session()
res = sess.post(url, auth=(username, password))
print(res.text)
#print(re.findall("<pre>\n(.*)",content)[0])
