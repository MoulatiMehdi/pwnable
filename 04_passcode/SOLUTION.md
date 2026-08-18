# Passcode

let disassemble the welcome and login functions : 

Dump of assembler code for function welcome:
```asm
080492f2 <welcome>:
 80492f2:       55                      push   %ebp
 80492f3:       89 e5                   mov    %esp,%ebp
 80492f5:       53                      push   %ebx
 80492f6:       83 ec 74                sub    $0x74,%esp
 80492f9:       e8 32 fe ff ff          call   8049130 <__x86.get_pc_thunk.bx>
 80492fe:       81 c3 02 2d 00 00       add    $0x2d02,%ebx
 8049304:       65 a1 14 00 00 00       mov    %gs:0x14,%eax
 804930a:       89 45 f4                mov    %eax,-0xc(%ebp)
 804930d:       31 c0                   xor    %eax,%eax
 804930f:       83 ec 0c                sub    $0xc,%esp
 8049312:       8d 83 63 e0 ff ff       lea    -0x1f9d(%ebx),%eax
 8049318:       50                      push   %eax
 8049319:       e8 32 fd ff ff          call   8049050 <printf@plt>
 804931e:       83 c4 10                add    $0x10,%esp
 8049321:       83 ec 08                sub    $0x8,%esp
 8049324:       8d 45 90                lea    -0x70(%ebp),%eax
 8049327:       50                      push   %eax
 8049328:       8d 83 75 e0 ff ff       lea    -0x1f8b(%ebx),%eax
 804932e:       50                      push   %eax
 804932f:       e8 9c fd ff ff          call   80490d0 <__isoc99_scanf@plt>
 8049334:       83 c4 10                add    $0x10,%esp
 8049337:       83 ec 08                sub    $0x8,%esp
 804933a:       8d 45 90                lea    -0x70(%ebp),%eax
 804933d:       50                      push   %eax
 804933e:       8d 83 7b e0 ff ff       lea    -0x1f85(%ebx),%eax
 8049344:       50                      push   %eax
 8049345:       e8 06 fd ff ff          call   8049050 <printf@plt>
 804934a:       83 c4 10                add    $0x10,%esp
 804934d:       90                      nop
 804934e:       8b 45 f4                mov    -0xc(%ebp),%eax
 8049351:       65 2b 05 14 00 00 00    sub    %gs:0x14,%eax
 8049358:       74 05                   je     804935f <welcome+0x6d>
 804935a:       e8 61 00 00 00          call   80493c0 <__stack_chk_fail_local>
 804935f:       8b 5d fc                mov    -0x4(%ebp),%ebx
 8049362:       c9                      leave  
 8049363:       c3                      ret 
```

Dump of assembler code for function login:
```asm
080491f6 <login>:
 80491f6:       55                      push   %ebp
 80491f7:       89 e5                   mov    %esp,%ebp
 80491f9:       56                      push   %esi
 80491fa:       53                      push   %ebx
 80491fb:       83 ec 10                sub    $0x10,%esp
 80491fe:       e8 2d ff ff ff          call   8049130 <__x86.get_pc_thunk.bx>
 8049203:       81 c3 fd 2d 00 00       add    $0x2dfd,%ebx
 8049209:       83 ec 0c                sub    $0xc,%esp
 804920c:       8d 83 08 e0 ff ff       lea    -0x1ff8(%ebx),%eax
 8049212:       50                      push   %eax
 8049213:       e8 38 fe ff ff          call   8049050 <printf@plt>
 8049218:       83 c4 10                add    $0x10,%esp
 804921b:       83 ec 08                sub    $0x8,%esp
 804921e:       ff 75 f0                push   -0x10(%ebp)
 8049221:       8d 83 1b e0 ff ff       lea    -0x1fe5(%ebx),%eax
 8049227:       50                      push   %eax
 8049228:       e8 a3 fe ff ff          call   80490d0 <__isoc99_scanf@plt>
 804922d:       83 c4 10                add    $0x10,%esp
 8049230:       8b 83 fc ff ff ff       mov    -0x4(%ebx),%eax
 8049236:       8b 00                   mov    (%eax),%eax
 8049238:       83 ec 0c                sub    $0xc,%esp
 804923b:       50                      push   %eax
 804923c:       e8 1f fe ff ff          call   8049060 <fflush@plt>
 8049241:       83 c4 10                add    $0x10,%esp
 8049244:       83 ec 0c                sub    $0xc,%esp
 8049247:       8d 83 1e e0 ff ff       lea    -0x1fe2(%ebx),%eax
 804924d:       50                      push   %eax
 804924e:       e8 fd fd ff ff          call   8049050 <printf@plt>
 8049253:       83 c4 10                add    $0x10,%esp
 8049256:       83 ec 08                sub    $0x8,%esp
 8049259:       ff 75 f4                push   -0xc(%ebp)
 804925c:       8d 83 1b e0 ff ff       lea    -0x1fe5(%ebx),%eax
 8049262:       50                      push   %eax
 8049263:       e8 68 fe ff ff          call   80490d0 <__isoc99_scanf@plt>
 8049268:       83 c4 10                add    $0x10,%esp
 804926b:       83 ec 0c                sub    $0xc,%esp
 804926e:       8d 83 31 e0 ff ff       lea    -0x1fcf(%ebx),%eax
 8049274:       50                      push   %eax
 8049275:       e8 16 fe ff ff          call   8049090 <puts@plt>
 804927a:       83 c4 10                add    $0x10,%esp
 804927d:       81 7d f0 e6 28 05 00    cmpl   $0x528e6,-0x10(%ebp)
 8049284:       75 48                   jne    80492ce <login+0xd8>
 8049286:       81 7d f4 c9 07 cc 00    cmpl   $0xcc07c9,-0xc(%ebp)
 804928d:       75 3f                   jne    80492ce <login+0xd8>
 804928f:       83 ec 0c                sub    $0xc,%esp
 8049292:       8d 83 3d e0 ff ff       lea    -0x1fc3(%ebx),%eax
 8049298:       50                      push   %eax
 8049299:       e8 f2 fd ff ff          call   8049090 <puts@plt>
 804929e:       83 c4 10                add    $0x10,%esp
 80492a1:       e8 da fd ff ff          call   8049080 <getegid@plt>
 80492a6:       89 c6                   mov    %eax,%esi
 80492a8:       e8 d3 fd ff ff          call   8049080 <getegid@plt>
 80492ad:       83 ec 08                sub    $0x8,%esp
 80492b0:       56                      push   %esi
 80492b1:       50                      push   %eax
 80492b2:       e8 09 fe ff ff          call   80490c0 <setregid@plt>
 80492b7:       83 c4 10                add    $0x10,%esp
 80492ba:       83 ec 0c                sub    $0xc,%esp
 80492bd:       8d 83 47 e0 ff ff       lea    -0x1fb9(%ebx),%eax
 80492c3:       50                      push   %eax
 80492c4:       e8 d7 fd ff ff          call   80490a0 <system@plt>
 80492c9:       83 c4 10                add    $0x10,%esp
 80492cc:       eb 1c                   jmp    80492ea <login+0xf4>
 80492ce:       83 ec 0c                sub    $0xc,%esp
 80492d1:       8d 83 55 e0 ff ff       lea    -0x1fab(%ebx),%eax
 80492d7:       50                      push   %eax
 80492d8:       e8 b3 fd ff ff          call   8049090 <puts@plt>
 80492dd:       83 c4 10                add    $0x10,%esp
 80492e0:       83 ec 0c                sub    $0xc,%esp
 80492e3:       6a 00                   push   $0x0
 80492e5:       e8 c6 fd ff ff          call   80490b0 <exit@plt>
 80492ea:       90                      nop
 80492eb:       8d 65 f8                lea    -0x8(%ebp),%esp
 80492ee:       5b                      pop    %ebx
 80492ef:       5e                      pop    %esi
 80492f0:       5d                      pop    %ebp
 80492f1:       c3                      ret    
```

scanf can accept only the first 100 character the rest are ignored.

`name` and `passcode1` owned by different functions but since the call of the functions are adjuscet to each other , they will have the same  resigter base pointer `$ebp` 

We can conclude that the address of  : 
- `name`      : $ebp-0x70 in welcome function
- `passcode1` : $ebp-0x10 in login function
- `passcode2` : $ebp-0xc  in login function




- the difference between `name` and `passcode1` is 0x60 (96), which means we need 96 non-null bytes characters to override the value of variable `passcode1`.
so with that in mind,we can change the value of `passcode1` variable to a real address to be able to change the value of it with `scanf`.

the question is : What should we change ?

if we disassemble any function after the `scanf`, we can see that it uses a variable to store real function address, 

for example in the function `fflush` , it use `jmp` to jump to the real fflush function saving its address in `0x804c014`.

```asm

 0x08049060 <fflush@plt>:
    0x8049060:       ff 25 14 c0 04 08       jmp    *0x804c014
    0x8049066:       68 10 00 00 00          push   $0x10
    0x804906b:       e9 c0 ff ff ff          jmp    8049030 <_init+0x30>

```

and since `jmp` jump to another section of code unconditionally

The idea is to use the function `scanf` of the `name` to change the value of `passcode1` variable, 
since scanf use the value of `passcode1`. and make equal to `0x804c014` the variable that store the function address (line fflush in this situation).

after that we uses the the second scanf to override the the value of `x804c014` to the address of the line where it execute the `system` function

and that's it.
