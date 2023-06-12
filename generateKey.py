from cryptography.fernet import Fernet

def keygen():
    key = Fernet.generate_key()

    # file1 = open("filekey.key", "w")

    # file1.write(str(key))

    # file1.close()

    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)

    print("Key written to filekey.key")

    return key