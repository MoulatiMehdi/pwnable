from pwn import *
import re


#context.log_level = "debug"



s = ssh(user="coin1",host="pwnable.kr",port=2222,password="guest")
shell = s.shell("/bin/bash")

list = [
    b'from pwn import *',
    b'import re',
    b'',
    b's = remote("0",10009)',
    b'',
    b's.recv().decode()',
    b'',
    b'',
    b'for i in range(0,100):',
    b'    line  = s.recv().decode()',
    b'    N,C=map(int,re.findall("N=(\\d+) C=(\\d+)",line)[0])',
    b'    start = 0',
    b'    end   = N',
    b'    while start <= end :',
    b'',
    b'        mid  = (start + end) // 2',
    b'        coins = " ".join([str(i) for i in range(start,mid + 1)])',
    b'        s.sendline(coins.encode())',
    b'',
    b'        line = s.recv()',
    b'        if line.startswith(b"Correct"):',
    b'            print(line.decode(),end="")',
    b'            break',
    b'',
    b'        num = int(line)',
    b'        if num % 10 == 0 :',
    b'            start = mid + 1',
    b'        else:',
    b'            end = mid',
    b'',
    b'print(s.recv(timeout=1).decode())',
    b'',
    b's.close()',
    b'EOF'
]

shell.sendline(b"cat << EOF > /tmp/file.py")
shell.sendlines(list)
shell.recv(timeout=3)


shell.sendline(b"python3 /tmp/file.py")

while True: 
    line = shell.recv(timeout=4)
    if not line: 
        break
    print(line.decode())

shell.close()
s.close()
