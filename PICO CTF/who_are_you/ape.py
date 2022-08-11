#!/usr/bin/env python3

import requests
import re

web = "http://mercury.picoctf.net:46199/"

headers = {
    'User-Agent': 'PicoBrowser',
    'Referer': 'http://mercury.picoctf.net:46199/',
    'Date': 'Wed, 16 Oct 2018 07:28:00 GMT',
    'DNT': '1',
    'X-Forwarded-For': '1.208.107.162',
    'Accept-Language': 'sv'

}

resp = requests.get(web, headers=headers).text
flag_sample = re.findall("<b>(.*)</b>", resp)
flag = "".join(flag_sample)
print("Your flag is " + flag)
