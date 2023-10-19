from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

key = get_random_bytes(16)
iv = get_random_bytes(16)


def encrypt_password(password, key, iv):
    password = password.encode()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(password, AES.block_size))
    return ciphertext


def decrypt_password(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted.decode()

password_to_encrypt = "my_secret_password"
encrypted_password = encrypt_password(password_to_encrypt, key, iv)
print(f"Encrypted Password: {encrypted_password}")

decrypted_password = decrypt_password(encrypted_password, key, iv)
print(f"Decrypted Password: {decrypted_password}")
