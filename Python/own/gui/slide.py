from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title = 'Slides'
root.geometry("400x400")

# vertical = Scale(root, from_=0, to=200)
# vertical.pack()

# def update_hori(var):
#     horizontal_get = Label(root, text=horizontal.get()).pack()
#     root.geometry(f"{horizontal.get()}x400")

# horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL, command=update_hori)
# horizontal.pack()


# button = Button(root, text='Click Me!', command=update_hori).pack()

var = StringVar()

def show():
    label = Label(root, text=var.get()).pack()

c = Checkbutton(root, text='Check this box', variable=var, onvalue='On', offvalue='Off')
c.deselect()
c.pack()

myButton = Button(root, text='Show Selection', command=show).pack()

options = [
    "Monday",
    "Tuesday",
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
]

clicked = StringVar()
clicked.set(options[0])
drop = OptionMenu(root, clicked, *options)
drop.pack()

def shows():
    my_Label = Label(root, text=clicked.get()).pack()

button = Button(root, text='Show Select', command=shows).pack()


mainloop()
