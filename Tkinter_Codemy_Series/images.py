from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Lets see icons')
#root.iconbitmap('/home/tareeq/Desktop/PyPro/FaceRecognizer/demoImages/known/Donald Trump.jpg')


my_img = ImageTk.PhotoImage(Image.open("/home/tareeq/Desktop/PyPro/FaceRecognizer/demoImages/known/Donald Trump.jpg"))
my_label = Label(image=my_img)
my_label.pack()


button_quit =Button(root,text="Exit Program", command = root.quit)
button_quit.pack()

root.mainloop()