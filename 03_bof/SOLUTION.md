```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void func(int key){
        char overflowme[32];
        printf("overflow me : ");
        gets(overflowme);       // smash me!
        if(key == 0xcafebabe){
                setregid(getegid(), getegid());
                system("/bin/sh");
        }
        else{
                printf("Nah..\n");
        }
}
int main(int argc, char* argv[]){
        func(0xdeadbeef);
        return 0;
}

```


when we run the gdb with the binary we can see that : 
the address of variables : 

- `overflowme` : $ebp-0x2c ($ebp - 44)
- `key`        : $ebp+0x8 ($ebp + 8)

the difference between `overflowme` and `key` is 

```44 + 8 = 52``` 

so we need to add 52 random characters + the payload  to solve this puzzle (the bytes of the `payload` should be backword because the byte-order of the cpu is little-endienne)


## NOTE: 

`$ebp` register , it seperate between the arguments  and the local variables of  the function. 
that's why : 

- `key`  have `$ebp+0x8`
- `overflowme`  have `$ebp-0x2c`

