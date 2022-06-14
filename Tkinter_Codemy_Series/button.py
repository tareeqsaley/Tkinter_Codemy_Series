from tkinter import *

root = Tk() #creates root window 

def myClick():
    myLabel = Label(root, text = "Look I clicked a button!")
    myLabel.pack()

myButton1 = Button(root, text = "dont click!", padx = 50, pady = 50, state = DISABLED) #pad for size, state for enabling button
myButton2 = Button(root, text = "click!", padx= 50, pady = 80, command=myClick, fg = "black", bg="red")

myButton1.pack()
myButton2.pack()

root.mainloop()