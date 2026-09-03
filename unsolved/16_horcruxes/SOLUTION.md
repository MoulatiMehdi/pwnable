its clear that the code contains `buffer overflow` with the `gets()` c function.

so we can use the `cyclic` function of the `pwntools` to detect the `stack frame` of the caller function and override it to all function from `A()` to `H()` 

and then return to the exact place where we give the answer, add up all the number to get the result.
