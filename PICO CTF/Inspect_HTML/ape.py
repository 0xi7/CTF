#!/usr/bin/env python3

import requests
import re

site = "http://saturn.picoctf.net:49386/"
web = requests.get(site).text

f = re.findall("<!--(.*)-->", web)
flag = "".join(f)
print(flag)
