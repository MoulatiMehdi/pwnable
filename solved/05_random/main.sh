#!/bin/bash 

set -e 

cd /tmp
cc -x c -o /tmp/rand - << EOF 
# include <stdio.h>
# include <stdlib.h>
void main ()
{
    printf("%d\n",rand());
}
EOF

cd /home/random
echo $(( $(/tmp/rand) ^ 0xcafebabe )) | /home/random/random

