#!/bin/python 

from __future__ import print_function

from pwn import * 

context.log_level = "error"

def is_valid(num : int):
    return num >= 0x20 and  num <= 0x7f 

def addr_valid (num : int ):
    return all(is_valid(x) for x in  num.to_bytes(4, "little")) 

def ascii_sym(filename : str,base : int) :
    print("--------------------")
    print(filename)
    elf = ELF(filename)
    for key in elf.symbols.keys(): 
        addr = int(elf.symbols[key]) + base
        if addr_valid(int(addr)):
            print(hex(addr),key);


ascii_sym('./libc-2.15.so',0x5555e000)
ascii_sym('./ascii_easy',0)
