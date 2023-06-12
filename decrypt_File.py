from cryptography.fernet import Fernet

# file1 = open("filekey.key", "r")

# key = file1.read()

# file1.close()

def Dec(root):
	with open('filekey.key', 'rb') as filekey:
		key = filekey.read()

	fernet = (Fernet(key))

	# opening the encrypted file
	with open(root.filename, 'rb') as enc_file:
		encrypted = enc_file.read()

	# decrypting the file
	decrypted = fernet.decrypt(encrypted)

	# opening the file in write mode and
	# writing the decrypted data
	with open(root.filename, 'wb') as dec_file:
		dec_file.write(decrypted)



