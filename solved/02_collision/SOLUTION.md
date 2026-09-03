the code make the sum the 5 numbers. 
when the array of `char` is casted to an array of `int` , each integer is composed of 4 character
and since the archtechture of the cpu is `little-endienne` the bytes order is reversed.

all the bytes should be different than null byte because the code uses `strlen` to calculate the size of the string 

if we considered that all the 16 bytes ares `0x01` , we can calculate the last number by subtract `0x04040404` from `0x21dd09ec`, which is the missing integer.
