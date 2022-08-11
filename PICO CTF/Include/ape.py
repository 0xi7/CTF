#!/usr/bin/env python3

import requests
import re


site1 = "http://saturn.picoctf.net:59300/script.js"
site2 = "http://saturn.picoctf.net:59300/style.css"

web = requests.get(site1).text
web2 = requests.get(site2).text

second_half = re.findall("//(.*)", web)
flag2 = "".join(second_half).replace(" ", "")
flag1 = web2[45:70]
flag = flag1 + flag2
print(flag)
