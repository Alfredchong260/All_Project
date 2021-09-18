from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()

def open():
    global my_img

    top = Toplevel()
    my_img = ImageTk.PhotoImage(Image.open('../lengluii/1f1f70a4183c5830bc6c964a2a974e76.jpg'))
    my_label = Label(top, image=my_img).pack()
    button2 = Button(top, text='Close window', command=top.destroy).pack()

def file():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir='./', title="Select a file",\
        filetypes=(('png files', '*.png'), ('all files', '*.*'), ('python file', '*.py'), ('jpg files', '*.jpg')))
    top = Toplevel()
    myLabel = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(top, image=my_image).pack()
    close_button = Button(top, text='Close Window', command=top.destroy).pack()

button = Button(root, text='Open a new window', command=open).pack()
button_1 = Button(root, text='Open File', command=file).pack()
button_close = Button(root, text='Close program', command=root.quit).pack()



mainloop()
