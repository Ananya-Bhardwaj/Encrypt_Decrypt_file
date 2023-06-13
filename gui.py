from tkinter import *
from tkinter import filedialog
from Encrypt_file import Enc
from Decrypt_File import Dec

root = Tk()
root.title('Encrypt_Decrypt File')
root.geometry("400x400")

def Encrypt():
    root.filename = filedialog.askopenfilename(title="Upload the file", filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
    Enc(root)
    myLabel = Label(root, text = "File encrypted sucessfully and key saved to filekey.key")
    myLabel.pack()

def Decrypt():
    root.filename = filedialog.askopenfilename(title="Upload the file", filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
    Dec(root)
    myLabel = Label(root, text="File has been decrypted successfully")
    myLabel.pack()


myButton1 = Button(root, text = "Encrypt File", command=Encrypt, fg="blue", bg="#000000")
myButton2 = Button(root, text = "Decrypt File", command=Decrypt, fg="blue", bg="#000000")

myButton1.pack()
myButton2.pack()

root.mainloop()
