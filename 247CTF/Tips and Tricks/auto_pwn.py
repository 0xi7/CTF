#!/usr/bin/env python3

from pwn import *

website = "9efcd51faf5b4746.247ctf.com"
port = 50351
s = remote(website, port)
print(s.recvline())
print(s.recvline())

for i in range(500):
    print("We are at range : " + str(i))
    question = s.recvline().decode("utf-8")
    a = int(question.split()[5])
    b = int(question.split()[7].strip("?"))
    #print(a)
    #print(b)
    sum = str(int(a) + int(b))
    total = (sum + "\r\n").encode("utf-8")
    s.sendline(total)
    s.recvline()

print(s.recvline().decode("utf-8"))
s.close()
