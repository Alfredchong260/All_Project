"""
打包也教吗 简单的会教

先听思路,课后自己敲

ctrl + f


1. 相对导入
2. tkinter设置样式是单个控件还是允许批量设置，像css这种
"""
import tkinter
# from tkinter import *  # 杜绝使用
import tkinter as tk  # as 别名

# root = tk.Tk()
root = tk.Tk()
root.geometry('500x300+100+100')
root.mainloop()
