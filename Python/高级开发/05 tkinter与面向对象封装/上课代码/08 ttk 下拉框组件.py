import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('500x300')
number_int_var = tk.StringVar()

# 创建一个下拉列表
numberChosen = ttk.Combobox(root, textvariable=number_int_var)

# 设置下拉列表的值
numberChosen['values'] = (1, 2, 4, 42, 100)

# 设置其在界面中出现的位置  column代表列   row 代表行
numberChosen.pack()

# 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
numberChosen.current(0)


def func():
    print(number_int_var.get())


tk.Button(root, text='打印选中内容', command=func).pack()

root.mainloop()
