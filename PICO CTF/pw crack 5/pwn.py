import hashlib

### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################

flag_enc = open('level5.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level5.hash.bin', 'rb').read()


def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()


def level_5_pw_check():
    with open("dictionary.txt", "r") as file:            ## Changed from here
        for pw in file:
            pw = pw.strip()
            user_pw_hash = hash_pw(pw)
            if( user_pw_hash == correct_pw_hash ):
                print("Welcome back... your flag, user:")
                decryption = str_xor(flag_enc.decode(), pw)
                print("The correct flag is = " + decryption)
                print("The correct password is = " + pw)
                return
        # print("That password is incorrect")
    file.close()                                            ## Changes finished here


level_5_pw_check()
