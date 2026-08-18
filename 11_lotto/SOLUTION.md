in the play function : 
```c
void play(){

        int i;
        printf("Submit your 6 lotto bytes : ");
        fflush(stdout);

        int r;
        r = read(0, submit, 6);

        printf("Lotto Start!\n");
        //sleep(1);

        // generate lotto numbers
        int fd = open("/dev/urandom", O_RDONLY);
        if(fd==-1){
                printf("error. tell admin\n");
                exit(-1);
        }
        unsigned char lotto[6];
        if(read(fd, lotto, 6) != 6){
                printf("error2. tell admin\n");
                exit(-1);
        }
        for(i=0; i<6; i++){
                lotto[i] = (lotto[i] % 45) + 1;         // 1 ~ 45
        }
        close(fd);

        // calculate lotto score
        int match = 0, j = 0;
        for(i=0; i<6; i++){
                for(j=0; j<6; j++){
                        if(lotto[i] == submit[j]){
                                match++;
                        }
                }
        }

        // win!
        if(match == 6){
                setregid(getegid(), getegid());
                system("/bin/cat flag");
        }
        else{
                printf("bad luck...\n");
        }
}

```
this loop - where the code calculate the lotto score - compare one character in the `lotto` array with every character in the `submit` array.
which means if by chance we manage to match  one character , the score will be 6.

and since the score should be 6, and `/dev/urandom` is high likely to not repeat characters. 
the best chance to solve it is by repeat a character 6 time between 1 ~ 45

