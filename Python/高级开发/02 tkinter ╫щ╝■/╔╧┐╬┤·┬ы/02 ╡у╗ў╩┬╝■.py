import tkinter as tk
import time
import datetime

root = tk.Tk()
root.geometry('500x300+100+100')

time_str = str(datetime.datetime.today())[:-7]  # [:-7] 切片语法 看实际的长度进行切片
# 0. 创建一个可变变量对象
# set 设置对象的字符串 --> 会绑定到GUI界面上 --> 更新页面上的值
# get 获取对象的字符串 --> 获取页面元素的值(label button entry) --> 打印到控制台
time_str_var = tk.StringVar()

time_str_var.set(time_str)

label = tk.Label(root, textvariable=time_str_var, font=('宋体', 20))
label.pack()

button = tk.Button(root, text='点我试试')
button.pack()


def button_click():
    print('按钮被点击了')
    print('当前页面上显示的时间为:\t', time_str_var)
    # 可变变量的值必须用 get 才能获取到
    print('当前页面上显示的时间为:\t', time_str_var.get())
    time_str_var.set('已经获取了时间')
    print('当前页面上显示的内容为:\t', time_str_var.get())


# 绑定点击事件 --> 点击按钮之后触发函数
button.config(command=button_click)
root.mainloop()
