import requests
import base64
import re
i = 1000000
m= 1000000
url= 'https://www.zego.com/password-reset-confirm/MTA0MTA4Ng/set-password'
res =requests.get(url)
content = res.text
print(content)