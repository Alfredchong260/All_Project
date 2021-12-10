import tkinter as tk
from tkinter import colorchooser

root = tk.Tk()
root.geometry('500x300')


def callback():
    color_name = colorchooser.askcolor(color='red', title='选择喜欢的颜色')
    print(color_name)


tk.Button(root, text="选择颜色", command=callback).pack()
root.mainloop()
