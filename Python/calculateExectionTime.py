import time
from wolfcrypt.hashes import HmacSha256
start = time.time()

phrase = "sarvesh"
key = "pass"
HmacSha256(key, phrase).hexdigest()

end = time.time()
print(end - start)
