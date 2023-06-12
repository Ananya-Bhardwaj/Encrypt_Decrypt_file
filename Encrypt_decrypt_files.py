from generateKey import keygen
from cryptography.fernet import Fernet
from tkinter import filedialog

# with open('filekey.key', 'wb') as filekey:
#    filekey.write(key)


# Open the file that contains the key.
# Initialize the Fernet object and store it in the fernet variable.
# Read the original file.
# Encrypt the file and store it into an object.
# Then write the encrypted data into the same file nba.csv.

# f = Fernet(key)

# file = open("file.txt", "r+")

# original = file.read()

# encrypted = f.encrypt(bytes(original))

# file.write(encrypted)

# file.close()
# using the generated key

def Enc(root):
   key = keygen(); 

   fernet = Fernet(key)
 
   # opening the original file to encrypt
   with open(root.filename, 'rb') as file:
      original = file.read()
     
   # encrypting the file
   encrypted = fernet.encrypt(original)
 
   # opening the file in write mode and
   # writing the encrypted data
   with open(root.filename, 'wb') as encrypted_file:
      encrypted_file.write(encrypted)

