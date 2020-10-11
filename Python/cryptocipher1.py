from Crypto.Cipher import Salsa20

key = b"0123456789012345"
cipher = Salsa20.new(key)
phrase = b"The secret I want to send"
ciphertext = cipher.encrypt(phrase)
print(ciphertext)
print(ciphertext.hex())
print(bytes.fromhex(ciphertext.hex()))
deciphertext = cipher.decrypt(bytes.fromhex(ciphertext.hex()))
print(deciphertext)
