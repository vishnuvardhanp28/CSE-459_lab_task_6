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

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("10.1.163.26", 5000))  # Use the server's IP address

    client_private_key = random.randint(1, 100)
    client_public_key = mod_exp(primitive_root, client_private_key, prime_modulus)

    server_public_key = int(client_socket.recv(1024).decode())

    client_socket.send(str(client_public_key).encode())

    client_shared_secret = mod_exp(server_public_key, client_private_key, prime_modulus)

    shared_key = hashlib.sha256(str(client_shared_secret).encode()).hexdigest()[:16]
    print("Shared secret:", client_shared_secret)

    encrypted_message = client_socket.recv(1024).decode()
    decrypted_message = xor_encrypt_decrypt(encrypted_message, shared_key)
    print("Decrypted message:", decrypted_message)

    client_socket.close()

if __name__ == "__main__":
    main()
