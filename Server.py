import socket
import random
import hashlib

def mod_exp(base, exp, mod):
    return pow(base, exp, mod)

def xor_encrypt_decrypt(data, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))

def main():
    prime_modulus = 23
    primitive_root = 5

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("10.1.163.26", 5000))  # Use your local machine's IP address
    server_socket.listen(1)
    print("Server waiting for client connection...")

    client_socket, client_address = server_socket.accept()
    print("Connection established with client:", client_address)

    server_private_key = random.randint(1, 100)
    server_public_key = mod_exp(primitive_root, server_private_key, prime_modulus)

    client_socket.send(str(server_public_key).encode())

    client_public_key = int(client_socket.recv(1024).decode())

    server_shared_secret = mod_exp(client_public_key, server_private_key, prime_modulus)

    shared_key = hashlib.sha256(str(server_shared_secret).encode()).hexdigest()[:16]
    print("Shared secret:", server_shared_secret)

    message = "Hello from Server!"
    encrypted_message = xor_encrypt_decrypt(message, shared_key)
    print("Encrypted message:", encrypted_message)

    client_socket.send(encrypted_message.encode())

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()
