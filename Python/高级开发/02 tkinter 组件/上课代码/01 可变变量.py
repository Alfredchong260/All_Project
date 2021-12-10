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
# 0.1 给对象设置初始化
time_str_var.set(time_str)

# 1. 创建一个 label 对象
# label = tk.Label(root, text=time_str, font=('宋体', 20))
label = tk.Label(root, textvariable=time_str_var, font=('宋体', 20))
label.pack()
# 死循环
while True:
    root.update()  # 显示页面,需要更新页面上的元素时使用 主动更新页面时使用
    time.sleep(1)
    # datetime.datetime.today 获取当前的时间,固定用法
    time_str = str(datetime.datetime.today())[:-7]
    # 0.2 不断更新可变变量里面的值
    time_str_var.set(time_str)
    print(time_str)
    # 将时间显示到页面上,然后再页面上不断更新

# 死循环运行完之后才会到这一句
root.mainloop()
