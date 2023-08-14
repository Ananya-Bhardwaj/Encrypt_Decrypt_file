from tkinter import *
from tkinter import filedialog
from Encrypt_file import Enc
from Decrypt_File import Dec

root = Tk()
root.title('Encrypt_Decrypt File')
root.geometry("400x400")

keyuser_var=StringVar()

def submit():

    keyuser=keyuser_var.get()

    #key entered by the user is saved in the variable keyuser
    #the entered key has to be compared with the key stored in the filekey.key file 

    with open(".key.csv", 'r') as file:
        csvreader = csv.reader(file)
        flag = False
        for row in csvreader:
            if (row[0]==root.filename and row[1][2:len(row[1])-1]==keyuser):
                Dec(root)
                myLabel = Label(root, text="File has been decrypted successfully")
                myLabel.pack()
                flag = True
        if flag==False:
            myLabel = Label(root, text="Wrong Key entered, file cannot be decrypted")
            myLabel.pack()

	
    keyuser_var.set("")


def Encrypt():
    root.filename = filedialog.askopenfilename(title="Upload the file", filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
    Enc(root)
    myLabel = Label(root, text = "File encrypted sucessfully and key saved to filekey.key")
    myLabel.pack()

def Decrypt():
    root.filename = filedialog.askopenfilename(title="Upload the file", filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
    key_user_entry = Entry(root, width=50, show = "*", textvariable=keyuser_var)
    submitButton = Button(root, text="Submit", command=submit, fg="blue", bg="#000000")
    key_user_entry.delete(0, END)
    key_user_entry.pack()
    submitButton.pack()


myButton1 = Button(root, text = "Encrypt File", command=Encrypt, fg="blue", bg="#000000")
myButton2 = Button(root, text = "Decrypt File", command=Decrypt, fg="blue", bg="#000000")

myButton1.pack()
myButton2.pack()

root.mainloop()

'''from tkinter import *
from tkinter import filedialog
from Encrypt_decrypt_files import Enc
from decrypt_File import Dec
import csv

root = Tk()
root.title('Encrypt_Decrypt File')
root.geometry("400x400")

keyuser_var=StringVar()

def submit():

    keyuser=keyuser_var.get()

    #key entered by the user is saved in the variable keyuser
    #the entered key has to be compared with the key stored in the filekey.key file 

    with open(".key.csv", 'r') as file:
        csvreader = csv.reader(file)
        flag = False
        for row in csvreader:
            if (row[0]==root.filename and row[1][2:len(row[1])-1]==keyuser):
                Dec(root)
                myLabel = Label(root, text="File has been decrypted successfully")
                myLabel.pack()
                flag = True
        if flag==False:
            myLabel = Label(root, text="Wrong Key entered, file cannot be decrypted")
            myLabel.pack()


    keyuser_var.set("")

def Encrypt():
    root.filename = filedialog.askopenfilename(title="Upload the file", filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
    Enc(root)
    myLabel = Label(root, text = "File encrypted sucessfully and key saved to filekey.key")
    myLabel.pack()

def Decrypt():
    root.filename = filedialog.askopenfilename(title="Upload the file", filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
    # key_user_var = StringVar()
    key_user_entry = Entry(root, width=50, show = "*", textvariable=keyuser_var)
    submitButton = Button(root, text="Submit", command=submit, fg="blue", bg="#000000")
    key_user_entry.pack()
    submitButton.pack()
    # key_user = key_user.get()
    # print(key_user)
    # Dec(root)
    # myLabel = Label(root, text="File has been decrypted successfully")
    # myLabel.pack()


myButton1 = Button(root, text = "Encrypt File", command=Encrypt, fg="blue", bg="#000000")
myButton2 = Button(root, text = "Decrypt File", command=Decrypt, fg="blue", bg="#000000")

myButton1.pack()
myButton2.pack()

root.mainloop()'''
