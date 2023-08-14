from generateKey import keygen
from cryptography.fernet import Fernet
from tkinter import filedialog

def Enc(root):
   # generating a key
   key = keygen(root); 
   
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

