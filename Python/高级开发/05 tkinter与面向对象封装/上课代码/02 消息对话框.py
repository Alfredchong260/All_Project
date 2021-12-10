import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry('500x300+150+150')

tk.Button(root, text="是或否", command=lambda: print(messagebox.askyesno(message='是否确认 ?'))).pack()
tk.Button(root, text="确认与取消", command=lambda: print(messagebox.askokcancel(title='选择', message='确认选择 ?'))).pack()
tk.Button(root, text="重试/取消", command=lambda: print(messagebox.askretrycancel(title='重试', message='重试 ?'))).pack()
tk.Button(root, text="是/否/取消", command=lambda: print(messagebox.askyesnocancel(title='询问', message='是/否/取消 ?'))).pack()
root.mainloop()
