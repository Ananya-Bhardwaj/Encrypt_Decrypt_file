from cryptography.fernet import Fernet
from csv import writer

def keygen(root):
    key = Fernet.generate_key()
    List = [root.filename, key]

    
    with open('key.csv', 'a') as filekey:
        writer_obj = writer(filekey)
        writer_obj.writerow(List)
        filekey.close()

    return key
