from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Message Box')


# showinfo, showwarning, showerror, askquestion, askyesno, askyesnocancel, askokcancel

def popup():
    response = messagebox.showerror("This is a PopUp!", "Hello World!")
    Label(root, text=response).pack()
    # if response == 'yes':
    #     Label(root, text='You Clicked Yes').pack()
    # else:
    #     Label(root, text='You Clicked No!').pack()

Button(root, text='PopUp', command=popup).pack()

mainloop()
