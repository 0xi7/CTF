#!/usr/bin/env python3
from string import ascii_uppercase as uppercase

flag_sample = []
numbers = [16,9,3,15,3,20,6,'{',20,8,5,14,21,13,2,5,18,19,13,1,19,15,14,'}']
for n in numbers:
    if type(n) == str:
        flag_sample.append(n)
    else:
        flag_sample.append(uppercase[n-1])
flag = ''.join(flag_sample)
print(flag)
