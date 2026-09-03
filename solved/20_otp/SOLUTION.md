the `./otp` program do the following things : 

- Read 16 bytes from /dev/urandam into `otp` variable 

- Create a filename from the first 8 bytes as integer  and concatenate it with /tmp/ : 
- Write the second 8 bytes into that file 
- Read again the same bytes from that file 
- compare it with the first argument after convert it to a number.



when we check the file with the `checksec` command , we found that the file is secured.
which means no shellcode , no bufferoverflow.


we can set how means byte can be read using one `read()` function with `ulimit` command 
with it , the read function will read nothing . but that will throw a signal `SIGXFSZ` (exceed file size), which  will terminal our binary.
we cann ignore it using the `trap` command before running the `./otp` program. 
and that's it


```bash 
ulimit -f 0
trap '' XFSZ 
./otp ""
```
