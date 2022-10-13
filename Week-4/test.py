from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

username = "test"
bUsername = str.encode(username)

cipherText = f.encrypt(bUsername)
print(cipherText)

plainText = f.decrypt(cipherText)
print(plainText)

de = plainText.decode()

print(de)