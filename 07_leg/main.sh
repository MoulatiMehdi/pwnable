#!/bin/bash

echo $((0x8cdc + 8 + 0x8d04 + 8 + 4 + 0x8d7c)) | ./leg 1<&0
