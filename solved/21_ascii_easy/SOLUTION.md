since we can pass only printable character as a argument to the `./ascii_easy` 
which means we need to use the `libc-2.15.so` binary to execute the shell with priviladge 

first we will search for the call of `execve()` instrcution , since call it will take the next bytes as arguments.



execve takes 3 argument : 
- `char * filename`
- `char ** argv`
- `char ** envp`



we can search an address that contains any string with null-byte at the end to be our filename , the rest can be an address point to `NULL`
this will make `execve` search for the file in the `PATH` variable 

and create symblink to the shell with the same name. 


and that is 
