## Checking the sha256sum and decyrpting the files with that

```bash
ctf-player@pico-chall$ cat checksum.txt 
3ad37ed6c5ab81d31e4c94ae611e0adf2e9e3e6bee55804ebc7f386283e366a4
ctf-player@pico-chall$ sha256sum files/* | grep 3ad37ed6c5ab81d31e4c94ae611e0adf2e9e3e6bee55804ebc7f386283e366a4
3ad37ed6c5ab81d31e4c94ae611e0adf2e9e3e6bee55804ebc7f386283e366a4  files/e018b574
ctf-player@pico-chall$ ./decrypt.sh files/e018b574
picoCTF{trust_but_verify_e018b574}
ctf-player@pico-chall$ 
```
