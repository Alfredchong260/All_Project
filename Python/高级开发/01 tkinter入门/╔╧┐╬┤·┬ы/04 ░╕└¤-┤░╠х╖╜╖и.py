""""""
"""
    创建一个窗口页面，需求如下
        标题为：青灯教育-学生信息管理系统
        位置：出现的位置为屏幕居中
        窗口大小为：500*300
"""
import tkinter as tk

root = tk.Tk()
root.title('青灯教育-学生信息管理系统')
# 出现的位置为屏幕居中
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 800
height = 500
x = screen_width / 2 - width / 2
y = screen_height / 2 - height / 2
size = f'{width}x{height}+{int(x)}+{int(y)}'

#
root.geometry(size)

root.mainloop()
