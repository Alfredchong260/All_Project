"""
    观看 辞职信.mp2 视频，完成页面布局及代码逻辑
    图片素材在 resignation 里面
"""
import tkinter as tk
from random import random
from tkinter import messagebox

root = tk.Tk()
root.geometry('500x300+100+100')
root['background'] = '#ffffff'

frame1 = tk.Frame(root, width=500, height=300, bg='#ffffff')
frame1.pack()

img = tk.PhotoImage(file='resignation/farewall.png')

tk.Label(frame1, text='尊敬的各位领导:', font=24, pady=30, padx=30, bg='#ffffff').pack(side=tk.LEFT, anchor=tk.N)

label_img = tk.Label(frame1, image=img, pady=30, padx=30, bd=0)
label_img.pack(side=tk.LEFT, anchor=tk.N)

tk.Label(frame1, text='辞职人：正心', height=25, font=24, padx=30, bg='#ffffff', anchor=tk.S).pack(side=tk.LEFT)

yes_img = tk.PhotoImage(file='resignation/yes.png')
no_img = tk.PhotoImage(file='resignation/no.png')

yes_btn = tk.Button(frame1, image=yes_img, bd=0)
yes_btn.place(relx=0.3, rely=0.8, anchor=tk.CENTER)

no_btn = tk.Button(frame1, image=no_img, bd=0)
no_btn.place(relx=0.7, rely=0.8, anchor=tk.CENTER)


def move(event):
    print(event)

    no_btn.place(relx=random(), rely=random(), anchor=tk.CENTER)


no_btn.bind('<Enter>', move)

# 同意之后的页面
frame2 = tk.Frame(root, width=500, height=300)
tk.Label(frame2, bg='#ffffff',
         text='老板大人，臣告退了\n这一退，可能就是一辈子了\n！！！！٩(๑>◡<๑)۶ ！！！！',
         font=('黑体', 18),
         justify="left",
         height=300,
         fg='red',
         padx=50
         ).pack()

tk.Button(frame2, bg='#ffffff', text='退出', command=root.quit).place(relx=0.9, rely=0.8)


def sure():
    frame1.pack_forget()
    frame2.pack()


yes_btn.config(command=sure)


def on_exit():
    messagebox.showwarning(title='提示', message='此路不通')


root.protocol("WM_DELETE_WINDOW", on_exit)
root.mainloop()
