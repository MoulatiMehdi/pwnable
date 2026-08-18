#!/bin/bash 


DEADBEEF=$'\xde\xad\xbe\xef'
CAFEBABE=$'\xca\xfe\xba\xbe'
PORT=1024

A=""
B=$'\x20\x0a\x0d'

VAL2="\x00\x0a\x00\xff\x00\x0a\x02\xff"

printf "\0\0\0\0" > $'\x0a'

printf "$VAL2" | env $DEADBEEF=$CAFEBABE "$HOME"/input2 {1..64} "$A" "$B"  $PORT {68..99} 2<&0  &


python3 << EOF 
import socket;
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
s.connect(('127.0.0.1',$PORT));
s.send(b'\xde\xad\xbe\xef');
EOF
