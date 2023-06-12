from tkinter import *
from tkinter import filedialog
from Encrypt_decrypt_files import Enc
from decrypt_File import Dec

root = Tk()
root.title('Encrypt_Decrypt File')
root.geometry("300x300")

keyuser_var=StringVar()

def Submit():
    keyuser = keyuser_var.get()
    print(keyuser)
    keyuser_var.set("")

def Encrypt():
    root.filename = filedialog.askopenfilename(initialdir="/Users", title="Upload the file", filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
    Enc(root)
    myLabel = Label(root, text = "File encrypted sucessfully and key saved to filekey.key")
    myLabel.pack()

def Decrypt():
    root.filename = filedialog.askopenfilename(initialdir="/Users", title="Upload the file", filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
    key_user_var = StringVar()
    key_user_entry = Entry(root, width=50, show = "*", textvariable=key_user_var)
    submitButton = Button(root, text="Submit", command=Submit, fg="blue", bg="#000000")
    key_user_entry.pack()
    submitButton.pack()
    # key_user = key_user.get()
    # print(key_user)
    Dec(root)
    myLabel = Label(root, text="File has been decrypted successfully")
    myLabel.pack()


myButton1 = Button(root, text = "Encrypt File", command=Encrypt, fg="blue", bg="#000000")
myButton2 = Button(root, text = "Decrypt File", command=Decrypt, fg="blue", bg="#000000")

myButton1.pack()
myButton2.pack()

root.mainloop()