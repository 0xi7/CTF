from pwn import *
import requests
import re

url = "https://jupiter.challenges.picoctf.org/problem/41511/"
session = requests.session()
content = session.get(url).text
web_first = re.findall('Anyways have 1/3 of the flag: (.*) -->', content)
first = "".join(web_first)

url2 = "https://jupiter.challenges.picoctf.org/problem/41511/mycss.css"
content2 = session.get(url2).text
web_second = re.findall("Here's part 2/3 of the flag: (.*) ", content2)
second = "".join(web_second)

url3 = "https://jupiter.challenges.picoctf.org/problem/41511/myjs.js"
content3 = session.get(url3).text
web_third = re.findall("Anyways part 3/3 of the flag: (.*) ", content3)
third = "".join(web_third)

sleep(3)
log.progress("Kindly wait until we get te flag for you!")

flag = first+second+third
print(flag)
