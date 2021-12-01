import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry('500x300+150+150')


def click():
    print('你按疼我了')


button = tk.Button(root, text='点我一下')
button.pack()
button.config(command=click)
tk.Button(root,
          text='信息提示',
          command=lambda: messagebox.showinfo(title='温馨提示', message='你的代码不符合规范')).pack()
tk.Button(root,
          text='警告',
          command=lambda: messagebox.showwarning(title='警告', message='你的代码可能会有问题')).pack()
tk.Button(root,
          text='错误提示',
          command=lambda: messagebox.showerror(title='错误', message='你的代码出现了bug')).pack()

root.mainloop()
