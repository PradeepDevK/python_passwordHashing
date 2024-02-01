from tkinter import *
import bcrypt

def validate(password):
    hash = b'$2b$12$9tzsTXqpXST6qpZOojKOUuGCYJMztVKVkQS99ctNWA4P8pcvEAYAu'
    password = bytes(password, encoding='utf-8')
    if bcrypt.checkpw(password, hash):
        print('Login Successfull')
    else:
        print('Invalid Password')

root = Tk()
root.geometry("500x500")

password_entry = Entry(root)
password_entry.pack()

button = Button(text="validate", command=lambda:validate(password_entry.get()))
button.pack()

root.mainloop()