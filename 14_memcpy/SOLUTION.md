(i can't test the binary `memcpy` because it works not like the binary inside the `nc`)
the problem is a alignment address problem ,when trying to use the registers of the floating point to copy the content of the string to another destination.
the instruction `movdqa` segfaults because the address is not 16bit aligned
