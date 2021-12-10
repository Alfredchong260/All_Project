import tkinter as tk
from tkinter import filedialog  # 文件对话框

root = tk.Tk()
root.geometry('500x300+150+150')

"""
    文件对话框
        1. 直接读取文件 (X )
        2. 获取文件的路径(√)
"""
tk.Button(root,
          text="获取文件名",
          command=lambda: print(filedialog.askopenfilename())).pack()
tk.Button(root,
          text="获取文件名(多个)",
          command=lambda: print(filedialog.askopenfilenames())).pack()
tk.Button(root,
          text="获取保存的文件名",  # 只是获取一个路径
          command=lambda: print(filedialog.asksaveasfilename())).pack()


def read_file():
    filename = filedialog.askopenfilename()
    print('filename:\t', filename)
    with open(filename, mode='r', encoding='utf-8') as f:
        print(f.read())


button = tk.Button(root, text='读取本地文件')
button.pack()
button.config(command=read_file)
info = "print('hello world !')"


def save_file():
    filename = filedialog.asksaveasfilename()
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(info)


button2 = tk.Button(root, text='保存内容到本地文件')
button2.pack()
button2.config(command=save_file)

root.mainloop()
