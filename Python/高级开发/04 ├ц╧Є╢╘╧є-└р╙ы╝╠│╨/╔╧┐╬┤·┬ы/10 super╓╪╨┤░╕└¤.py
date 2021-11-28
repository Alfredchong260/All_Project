"""
    修改默认的 tk.Frame 组件的 pack 布局方式，
    使其在布局之前先打印 `当前组件正在布局中`，布局完之后打印 `布局已完成`

    修改默认组件的表达形式
"""
import tkinter as tk

root = tk.Tk()
root.geometry('500x300+150+150')


class LoginFrame(tk.Frame):
    def __init__(self):
        super(LoginFrame, self).__init__()
        print('1. 登录布局已经创建')

    def pack(self):
        super(LoginFrame, self).pack()
        print('2. 登录布局已经布局完毕')


frame = LoginFrame()
# frame = tk.Frame()
# print('1. 当前组件正在布局中......')
frame.pack()
# print('2. 布局已完成')

root.mainloop()
