in this puzzle , you should learn the write an assembly code. 


`read()` function stops when : 
 - found a newline (only for stdin) 
 - found eof
 - reaches the buffer size 

so instead of pushing filename characters to the stack , we can read from the stdin the filename. 
and then reading the file content


## NOTES : 

### registers :

| 64-bit | 32-bit | 16-bit | 8-bit  |
| ------ | ------ | ------ | ------ |
| `RAX`  | `EAX`  | `AX`   | `AL`   |
| `RBX`  | `EBX`  | `BX`   | `BL`   |
| `RCX`  | `ECX`  | `CX`   | `CL`   |
| `RDX`  | `EDX`  | `DX`   | `DL`   |
| `RSI`  | `ESI`  | `SI`   | `SIL`  |
| `RDI`  | `EDI`  | `DI`   | `DIL`  |
| `RBP`  | `EBP`  | `BP`   | `BPL`  |
| `RSP`  | `ESP`  | `SP`   | `SPL`  |
| `R8`   | `R8D`  | `R8W`  | `R8B`  |
| `R9`   | `R9D`  | `R9W`  | `R9B`  |
| `R10`  | `R10D` | `R10W` | `R10B` |
| `R11`  | `R11D` | `R11W` | `R11B` |
| `R12`  | `R12D` | `R12W` | `R12B` |
| `R13`  | `R13D` | `R13W` | `R13B` |
| `R14`  | `R14D` | `R14W` | `R14B` |
| `R15`  | `R15D` | `R15W` | `R15B` |


- `RSP` the register stack pointer
- `RBP` the register base pointer (in linux : `RBP` > `RSP`) 
- `RAX` register means : 
   - the system call number that `syscall` will run
   - the return value of the system call after the `syscall`
- `RDI` the 1st argument 
- `RSI` the 2nd argument
- `RDX` the 3th argument
- `RCX` the 4th argument 


###  syscall numbers : 

| Syscall      | Number |
| ------------ | -----: |
| `read`       |    `0` |
| `write`      |    `1` |
| `open`       |    `2` |
| `close`      |    `3` |
| `stat`       |    `4` |
| `mmap`       |    `9` |
| `munmap`     |   `11` |
| `dup`        |   `32` |
| `dup2`       |   `33` |
| `socket`     |   `41` |
| `connect`    |   `42` |
| `accept`     |   `43` |
| `bind`       |   `49` |
| `listen`     |   `50` |
| `fork`       |   `57` |
| `execve`     |   `59` |
| `exit`       |   `60` |
| `kill`       |   `62` |
| `getuid`     |  `102` |
| `setuid`     |  `105` |
| `geteuid`    |  `107` |
| `seteuid`    |  `117` |
| `exit_group` |  `231` |



### instruction

`mov <dest> <src>` : move a value from `dest` to `src`
`xor` <v1> <v2>    : perform `XOR` bitwise operation and save it in `v1` 
`syscall`          : enter the linux kernel to perform a `syscall`

