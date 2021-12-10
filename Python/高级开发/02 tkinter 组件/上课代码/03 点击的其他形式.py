import tkinter as tk
import time
import datetime

root = tk.Tk()
root.geometry('500x300+100+100')

time_str = str(datetime.datetime.today())[:-7]  # [:-7] 切片语法 看实际的长度进行切片
time_str_var = tk.StringVar()

time_str_var.set(time_str)

label = tk.Label(root, textvariable=time_str_var, font=('宋体', 20))
label.pack()

button = tk.Button(root, text='点我试试')
button.pack()


def button_click():
    print('按钮被点击了')


# 1. 使用按钮对象绑定事件的 (可以将页面布局与代码逻辑进行分离)
button.config(command=button_click)
# button['command'] = button_click  # 不是面向对象的写法,不推荐

# def button_click():
#     print('按钮被点击了')
#
#
# # 2. 在创建对象的时候绑定事件
# button = tk.Button(root, text='点我试试', command=button_click)
# button.pack()

root.mainloop()
