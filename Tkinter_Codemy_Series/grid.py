from tkinter import *

root = Tk() #creates root window

myLabel1 = Label(root, text = "Hello World!") #creates label widget to be inserted in root window
myLabel2 = Label(root, text = "My name is Tareeq!") #creates label widget to be inserted in root window
myLabel3 = Label(root, text = "                   ") #creates label widget to be inserted in root window

myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 3)
myLabel3.grid(row = 1, column = 2)

root.mainloop()