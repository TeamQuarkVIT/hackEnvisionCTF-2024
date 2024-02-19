# One time use

- Name: One Time Use
- Author : kavigihan (community)

## Desc 
> Sometimes, long names are the only way to get in.


# Writeup

- We are given the `server.py` so let's take a look at what it does.

```python
def handle_client(client_socket, client_address):
    try:
        print(f"Accepted connection from {client_address}")
        
        random_key = urandom(16)
        random_iv = urandom(16)

        with open("flag", "r") as flag_file:
            flag_content = flag_file.read()

        enc_flag = encrypt(flag_content, random_key, random_iv)

        client_socket.send(b"Hey Stranger!, What is your name?\n")
        client_socket.send(b"")
        name = client_socket.recv(1024).decode().strip()
        
        if not name:
            client_socket.close()
            
        enc_msg = encrypt(name, random_key, random_iv)
        
        client_socket.send(f"Hello {name}! I am going to call you {enc_msg}!\n".encode())

        client_socket.send(b"\nHere is your New Year's present!\n")
        client_socket.send(enc_flag.encode())
        client_socket.close()

        print(f"Connection from {client_address} closed")
    except Exception as e:
        client_socket.close()
```

- Here we see when we connect to the server, its accepting the connection and asks us for our name. Once we provide our name, it is then encrypted and sent back to us along with a `Hello` message. Then the flag is read in from a file and then it's also encrypted and sent back to us.
- Here, the vulnerability being the same `key` and `iv` is used to encrypt both of them. Given that this is using AES in CTR mode, we can easily figure out the actual flag by xoring the encrypted flag with the xored blob of the name and its cipher.
- First let's connect and sent in a name,

```bash
➜  One_time_use nc 127.0.0.1 1337
Hey Stranger!, What is your name?
KavishkaGihanFernando
Hello KavishkaGihanFernando! I am going to call you p5E3cXvSURXSRTnBGECWa74+/KMq!

Here is your New Year's present!
pJEycFDBfDXeaQ7mOke0ZNo=
```
- Here the encrypted username is `p5E3cXvSURXSRTnBGECWa74+/KMq` and the encrypted flag is `pJEycFDBfDXeaQ7mOke0ZNo=`
- Using these we can figure out the flag with this simple script.

```python
import base64
from pwn import xor

msg = b'KavishkaGihanFernando'
enc_msg = 'p5E3cXvSURXSRTnBGECWa74+/KMq'
enc_flag = 'pJEycFDBfDXeaQ7mOke0ZNo='
blob = xor(base64.b64decode(enc_msg),base64.b64decode(enc_flag))
flag = xor(blob, msg)
print(flag)
```

