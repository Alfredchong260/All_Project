import tkinter as tk

root = tk.Tk()
root.geometry('500x300')

frame = tk.Frame(root, width=200, height=150, bg='cyan')


def mouse_entry(event):
    print(event)
    print('鼠标进入或退出的布局组件')


frame.bind("<Enter>", mouse_entry)
frame.bind("<Leave>", mouse_entry)
frame.pack()


def key_press(event):
    print(event)
    # 发生了什么事情,在哪里发送的,事件的特征是什么
    print(dir(event))
    print(event.keycode, type(event.keycode))
    if event.keycode == 65:
        frame.pack_forget()
    if event.keycode == 66:
        frame.pack()


# a 按下的时候 frame 隐藏
# b 按下的时候 frame 显示出来
root.bind("<Key>", key_press)
root.mainloop()
