import tkinter as tk

root = tk.Tk()
root.geometry('500x300')

frame = tk.Frame(root, width=200, height=150, bg='cyan')


def callback(event):
    print(event)
    print(type(callback))


def mouse_entry(event):
    print(event)
    print('鼠标进入或退出的布局组件')


def key_press(event):
    print(event)
    print('键盘被按下了')


# 绑定事件
frame.bind("<Button-1>", callback)
frame.bind("<Enter>", mouse_entry)
frame.bind("<Leave>", mouse_entry)
frame.pack()

root.bind("<Key>", key_press)
root.mainloop()
