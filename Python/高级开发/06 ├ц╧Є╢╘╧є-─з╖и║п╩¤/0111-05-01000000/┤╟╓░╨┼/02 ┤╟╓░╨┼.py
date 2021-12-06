""""""
"""
    观看 辞职信.mp2 视频，完成页面布局及代码逻辑
    图片素材在 resignation 里面
"""
import tkinter as tk
from random import random
from tkinter import messagebox
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry('500x300+100+100')
root['background'] = '#ffffff'
"""在这里实现具体的逻辑"""
font = ('宋体', 16)
info_label = tk.Label(root, text='尊敬的各位领导:', font=font)
info_label.pack(side=tk.LEFT, anchor=tk.N)

photo = ImageTk.PhotoImage(Image.open('resignation/farewall.png'))

photo_label = tk.Label(root, image=photo)
photo_label.pack(side=tk.LEFT, anchor=tk.N)

info_label = tk.Label(root, text='辞职人:正心', font=font)
info_label.pack(side=tk.LEFT, anchor=tk.S)

yes_photo = ImageTk.PhotoImage(Image.open('resignation/yes.png'))
no_photo = ImageTk.PhotoImage(Image.open('resignation/no.png'))

yes_btn = tk.Button(root, image=yes_photo)
yes_btn.place(relx=0.3, rely=0.8, anchor=tk.CENTER)
no_btn = tk.Button(root, image=no_photo)
no_btn.place(relx=0.7, rely=0.8, anchor=tk.CENTER)


def callback(event):
    print('当前位置', event.x, event.y)
    random_x = random()
    random_y = random()
    print('新位置', random_x, random_y)
    no_btn.place(relx=random_x, rely=random_y, anchor=tk.CENTER)


no_btn.bind('<Enter>', callback)


# 关闭默认的退出事件
def on_exit():
    messagebox.showwarning(title='提示', message='此路不通')


# 重新实现关闭的时间
root.protocol("WM_DELETE_WINDOW", on_exit)

root.mainloop()
