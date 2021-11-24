from tkinter import *

root = Tk()
root.title('Frames')

frame = Label(root, padx=50, pady=50, bd=2, bg='red')
frame.pack(padx=100, pady=100)

b = Button(frame, text='Don\'t click here', command=root.quit)
b.pack()

# r = IntVar()
# r.set("2")

MODES = [
    ("Pizza", "Pizza"),
    ("Cheese", "Cheese"),
    ("Pasta", "Pasta"),
    ("Onion", "Onion"),
]

pizz = StringVar()
pizz.set('Pizza')

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizz, value=mode, font=('', 15)).pack()

r = IntVar()

def click(value):
    global myLabel
    myLabel.pack_forget()
    myLabel = Label(root, text=value)
    myLabel.pack()

# Radiobutton(root, text='Option 1', variable=r, value=1, command=lambda: click(r.get())).pack()
# Radiobutton(root, text='Option 2', variable=r, value=2, command=lambda: click(r.get())).pack()

myLabel = Label(root, text=pizz.get())
myLabel.pack()

myButton = Button(root, text='Click Me!', command=lambda: click(pizz.get()))
myButton.pack()

root.mainloop()
