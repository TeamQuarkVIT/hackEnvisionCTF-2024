import warnings
import socket, sys
import threading
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from os import urandom
from base64 import b64encode

CONCURRENT_CLIENTS = 20

warnings.filterwarnings("ignore", category=RuntimeWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)


def encrypt(message, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(message.encode()) + encryptor.finalize()
    encrypted_message = ciphertext

    return b64encode(encrypted_message).decode()


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

        client_socket.send(b"\nHere is your present!\n")
        client_socket.send(enc_flag.encode())
        client_socket.close()

        print(f"Connection from {client_address} closed")
    except Exception as e:
        print(e)
        client_socket.close()

def main():
    global CONCURRENT_CLIENTS
    

    
    host = '0.0.0.0'
    port = int(sys.argv[1])

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(CONCURRENT_CLIENTS)
    print(f"Listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} <port>") 
        exit(1)
    try:
        main()
    except:
        main()
