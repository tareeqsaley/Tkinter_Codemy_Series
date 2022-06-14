from tkinter import *

root = Tk() #creates root window 

e = Entry(root, width = 50, bg = "grey", borderwidth = 5)
e.pack()
e.insert(0,"Enter Your Name")

def myClick():
    greeting = "Hello " + e.get()
    myLabel = Label(root, text = greeting)
    myLabel.pack()

myButton1 = Button(root, text = "click!",  command=myClick,)

myButton1.pack()


root.mainloop()