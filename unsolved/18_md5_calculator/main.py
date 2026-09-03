from pwn import *
import re

from pwnlib.elf import byte



s = ssh(user="md5calculator",host="pwnable.kr",port=2222,password="guest")
sh = s.shell("nc 0 10018") 


line =sh.recvlines(2)[1].decode() 
number = int(re.findall(r'-?\d+',line)[0])

sh.sendline(str(number).encode())


print(sh.recv(timeout=1).decode())

payload : bytes = b"hello";
sh.sendline(payload)


print(sh.recv(timeout=1).decode())


