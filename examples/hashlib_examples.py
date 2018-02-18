import hashlib
#Create a SHA-256 hash object
m = hashlib.sha256(b'Hello')
#Update the hash object with a buffer of bytes
m.update(b"Nobody inspects")
#Update the object a second time
m.update(b" the spammish repetition")
#Print the digest of the hash object's information so far (in bytes)
print(m.digest())
#Similar to digest(), but instead returns a string object of double length, containing only hexadecinal characters
print(m.hexdigest())
#Size of the resulting hash in bytes
print(m.digest_size)
#The internal block size of the hash algorithm in bytes
print(m.block_size)