from wolfcrypt.ciphers import Aes, MODE_CBC
import base64
from wolfcrypt.hashes import HmacSha256
import time

start = time.time()

cipher = Aes(b'Qb3d4LDracwKKLrBqB6WuSMOIlviHk9z',
             MODE_CBC, b'BeYKmsqjqNMgjAHG')

passphrase = '8f82ac00ae2642b332673ce73f145339581a503ea6459c553bcfbdfa49d2db72'

# secretkey = "".join(choice(string.ascii_letters + string.digits)
#                     for x in range(16))

secretkey = "uRys4rpJVs0s9qDD"

newphrase1 = HmacSha256(secretkey, passphrase).hexdigest()
# print("newphrase1", newphrase1)

encodedPhrase = base64.b64encode(cipher.encrypt(newphrase1))
encodedKey = base64.b64encode(cipher.encrypt(secretkey))
print("encodedPhrase", encodedPhrase)
print("encodedKey", encodedKey)


decipherPhase = cipher.decrypt(base64.b64decode(encodedPhrase))
decipherKey = cipher.decrypt(base64.b64decode(encodedKey))
# print("decipherPhase", decipherPhase)
# print("decipherKey", decipherKey)


newphrase2 = HmacSha256(decipherKey, passphrase).hexdigest()
# print("newphrase2", newphrase2)
print(decipherPhase == newphrase2)

end = time.time()
print(end - start)
