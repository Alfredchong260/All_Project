import tkinter as tk
from tkinter import messagebox


def on_exit():
    """当点击退出时，这个函数会被触发"""
    if messagebox.askyesno("退出", "确认退出程序?"):
        root.destroy()


root = tk.Tk()
root.geometry('500x300+100+100')
root.title('重新关闭事件')

root.protocol("WM_DELETE_WINDOW", on_exit)

root.mainloop()
