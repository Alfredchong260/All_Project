""""""
"""
    观看 辞职信.mp4 视频，完成页面布局及代码逻辑
    图片素材在 resignation 里面
"""


"""在这里实现具体的逻辑"""

from tkinter import messagebox
from random import random
from tkinter import *


class Leave:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('500x350+100+100')
        self.root['background'] = '#ffffff'
        self.root.resizable(0, 0)

        self.background = PhotoImage(file='./resignation/farewall.png')

        self.whole_frame = Frame(self.root, bg='#ffffff')
        self.whole_frame.pack()

        self.root.protocol("WM_DELETE_WINDOW", self.on_exit)
        self.create_page()

        self.root.mainloop()

    def disagree_call(self, event):
        x = random()
        y = random()
        self.disagree.place(relx=x, rely=y)

    def agree_com(self):
        self.whole_frame.pack_forget()
        self.new_page()

    def new_page(self):
        new_frame = Frame(self.root, background='#ffffff')
        new_frame.pack()
        Label(new_frame, text='', height=5, background='#ffffff').pack()
        Label(new_frame, text='老板，臣告退\n此次告退可能就是一辈子了\n(ﾉ*･ω･)敬礼ﾉ',
              font=('', 15), background='#ffffff').pack()
        Label(new_frame, text='', background='#ffffff').pack()
        Button(new_frame, text='退出', background='#ffffff', foreground='blue', activebackground='#DCDCDC', font=(
            '', 15), highlightbackground="blue", highlightcolor="blue", highlightthickness=2, command=self.root.destroy).pack(anchor=E)

    def create_page(self):
        Label(self.whole_frame, text='尊敬的各位领导：', font=(
            '', 15), background='#ffffff').grid(row=1, column=1)
        Label(self.whole_frame, image=self.background).grid(row=2, column=2)

        agree = Button(self.whole_frame, text='同意', background='#ffffff', foreground='blue', activebackground='#DCDCDC', font=(
            '', 15), highlightbackground="blue", highlightcolor="blue", highlightthickness=2, bd=0, width=6, command=self.agree_com)

        agree.grid(row=3, column=2, sticky=W)

        self.disagree = Button(self.whole_frame, text='不同意', background='#ffffff', foreground='red', activebackground='#DCDCDC', font=(
            '', 15), highlightbackground="red", highlightcolor="red", highlightthickness=2, bd=0, width=6)

        self.disagree.place(relx=0.55, rely=0.76)
        self.disagree.bind('<Enter>', self.disagree_call)

        Label(self.whole_frame, text='辞职人：小明', font=(
            '', 15), background='#ffffff').grid(row=4, column=3)


# 关闭默认的退出事件


    def on_exit(self):
        messagebox.showwarning(title='提示', message='此路不通')


Leave()
