import requests
import re


username = 'natas3'
password = 'sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'
url = 'http://%s.natas.labs.overthewire.org/s3cr3t/users.txt'%username
res= requests.get(url,auth=(username,password))
content = res.text
#print(content)
print(re.findall("natas4:(.*)", content)[0])