after decompile the `./brainfuck` binary, we found that : 

- there is no buffer overflow 
- the input takes 1024 characters 
- the input is saved at the variable `p` and its value is `tape` which are both in the global scope
- in the `do_brainfuck` function, there are instruction that : 
    - can decrement/increment the address
    - can decrement/increment the value
    - can set a byte at the current address
    - print the current byte in the current address

if we see around the `p` variable , we can reach `.plt` section that jump to the `.got`
we that in mind, we can change the address that the function jump to , and set it to any function we desire. 


but the problem is , how we can open a shell to read the flag? 

well , we can exploit the position of the `libc` inside our binary.
if we print the address of a function at runtime and we subtract it from the offset that exist in the `libc` , we can find the base pointer of the `libc`
and we that , we can find the exact position of the `system` function inside the `libc` and call our shell.


the only candidate that are simulare to system : 
- puts 
- memset 
- fgets

puts already contains a string from `.rodata` , which means its useless 
memset and fgets are already called.

if we call restart our main so that we can use the memset and fgets.
and this is where we should call the `_start` function.

so by setting any function to `_start` ( in our case  `putchar`)
and `memset` to `gets`  : to insert the argument for the system
amd `fgets` to `system` : to run the argument 


we can read the file
