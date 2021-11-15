from tkinter import *

root = Tk()
root.geometry('530x100')
root.config(bg='gray17')
root.overrideredirect(True)

def move(event):
    root.geometry(f'+{event.x_root}+{event.y_root}')


title_bar = Frame(root, bg='gray17', relief='raised')
title_bar.pack(side=TOP, fill=BOTH)
title_bar.bind('<B1-Motion>', move)

title = Label(title_bar, text='Code', bg='gray17', fg='lime', bd=2)
title.pack(side=LEFT)

close_btn = Button(title_bar, text='  x  ', command=root.destroy,
                   bg='gray17', fg='red', font=('', 15))
close_btn.pack(side=RIGHT)

min_btn = Button(title_bar, text='  -  ', bg='gray17', fg='skyblue', font=('', 15))
min_btn.pack(side=RIGHT)

mainloop()
