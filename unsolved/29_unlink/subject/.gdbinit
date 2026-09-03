layout asm
layout reg
break unlink
break *main+213
start < /tmp/f
set disassembly-flavor intel
define stack_func
    set $addr = $ebp
    while $addr > $esp
        printf "ebp-0x%02x: 0x%08x\n", $ebp-$addr, *(unsigned int *)$addr
        set $addr = $addr - 4
    end
end
