from tkinter import *
import requests


root = Tk()

def myclick():
    mylabel3 = Label(root, text = f"Hello {e.get()} ")
    mylabel3.grid(row = 3, column = 2)

e = Entry(root, width = 20, borderwidth = 3)
e.grid(row = 2, column = 1)
e.insert(0, "Enter Your name:")

myLabel1 = Label(root, text = "Helllo World!")
myLabel1.grid(row = 0, column = 0)

myLabel2 = Label(root, text = "My name is Mason")
myLabel2.grid(row = 1, column = 1)

mybutton = Button(root, text="Enter your name!",
                  padx=10, pady=10, command=myclick,
                  fg="white", bg="black")
mybutton.grid(row = 2 , column = 2)

root.mainloop()
