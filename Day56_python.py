#Implementation of Simple DES
print ("\nSubi - Day 56 of #100DaysOfCode\n") 
print("\nImplementation of Simple DES\n")

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def des_encrypt(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_plaintext = pad(plaintext, 8)  
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def des_decrypt(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = cipher.decrypt(ciphertext)
    plaintext = unpad(decrypted_text, 8)  
    return plaintext

key = b'01234567'
plaintext = b'This is a test'
ciphertext = des_encrypt(key, plaintext)
decrypted_text = des_decrypt(key, ciphertext)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted text:", decrypted_text)


#Implementation of Simple AES
print ("\nImplementation of Simple AES\n") 

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)

cipher = AES.new(key, AES.MODE_EAX)

plaintext = b'Hello, World!'
ciphertext, tag = cipher.encrypt_and_digest(plaintext)

decrypt_cipher = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
decrypted_plaintext = decrypt_cipher.decrypt_and_verify(ciphertext, tag)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted plaintext:", decrypted_plaintext)