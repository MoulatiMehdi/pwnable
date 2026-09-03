#!/opt/pyenv/shims/python
from pwn import *

elf = ELF("../libc-2.15.so")

for obj in elf.search(b"h"):
    print(obj)

