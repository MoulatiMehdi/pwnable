from pwn import * 

context.log_level = "error"

def is_valid(num : int):
    return num >= 0x20 and  num <= 0x7f 

def addr_valid (num : int ):
    return all(is_valid(x) for x in  num.to_bytes(4, "little")) 

def ascii_rop(filename : str,base : int) :
    print("--------------------")
    print(filename)
    rop = ROP(ELF(filename)).gadgets

    for key in rop.keys(): 
        addr = int(key) + base
        if addr_valid(int(addr)):
            print(f"0x{addr:08x}",";".join(rop[key].insns))


ascii_rop('./libc-2.15.so',0x5555e000)
ascii_rop('./ascii_easy',0)
