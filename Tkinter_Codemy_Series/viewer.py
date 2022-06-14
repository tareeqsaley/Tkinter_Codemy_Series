from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.title('Lets see icons')
#root.iconbitmap('/home/tareeq/Desktop/PyPro/FaceRecognizer/demoImages/known/Donald Trump.jpg')


image_1 = ImageTk.PhotoImage(Image.open("/home/tareeq/Desktop/PyPro/FaceRecognizer/demoImages/known/Donald Trump.jpg"))
image_2 = ImageTk.PhotoImage(Image.open("/home/tareeq/Desktop/PyPro/FaceRecognizer/demoImages/known/Nancy Pelosi.jpg"))
image_3 = ImageTk.PhotoImage(Image.open("/home/tareeq/Desktop/PyPro/FaceRecognizer/demoImages/known/Mike Pence.jpg"))
image_4 = ImageTk.PhotoImage(Image.open("/home/tareeq/Desktop/PyPro/FaceRecognizer/demoImages/known/Anthony Fauci.jpg"))

image_list = [image_1, image_2, image_3, image_4]   
image_number=0     
        
my_label = Label(image=image_1)
my_label.grid(row = 0,column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])


    button_forward = Button(root,text =">>" ,command = lambda:forward(image_number+1))
    button_back = Button (root,text = "<<", command =lambda:back(image_number-1))

    if image_number == 3:
         button_forward = Button(root,text =">>" , state = DISABLED)

    my_label.grid(row =0,column=0,columnspan=3)
    button_back.grid(row =1, column = 0)
    button_forward.grid(row =1, column = 2)


def back(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])


    button_forward = Button(root,text =">>" ,command = lambda:forward(image_number+1))
    button_back = Button (root,text = "<<", command =lambda:back(image_number-1))

    if image_number == 0:
         button_back = Button(root,text ="<<" , state = DISABLED)

    my_label.grid(row =0,column=0,columnspan=3)
    button_back.grid(row =1, column = 0)
    button_forward.grid(row =1, column = 2)





button_back = Button(root, text = "<<", command =lambda:back(image_number))
button_forward = Button(root,text =">>" ,command = lambda:forward(image_number))
button_quit =Button(root,text="Exit Program", command = root.quit)


button_back.grid(row =1, column = 0)
button_quit.grid(row =1, column = 1)
button_forward.grid(row =1, column = 2)


root.mainloop()