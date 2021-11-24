""""""
"""
    创建一个窗口页面，需求如下
        标题为：青灯教育-学生信息管理系统
        位置：出现的位置为屏幕居中
        窗口大小为：500*300
    当点击登录之后,收集学员的信息
"""

import tkinter as tk

root = tk.Tk()
root.geometry('500x300+100+100')
font = ('宋体', 18)

username_str_var = tk.StringVar()
password_str_var = tk.StringVar()

tk.Label(root, text='', font=font, width=5, height=3).grid(row=0, column=0)
tk.Label(root, text='用户名:', font=font).grid(row=1, column=1, padx=10, pady=10)
tk.Entry(root, font=font, textvariable=username_str_var).grid(row=1, column=2, padx=10, pady=10)
tk.Label(root, text='密 码:', font=font).grid(row=2, column=1, padx=10, pady=10)
tk.Entry(root, font=font, textvariable=password_str_var).grid(row=2, column=2, padx=10, pady=10)

# 没有第三行,后面的就会上移
submit = tk.Button(root, text='提交', font=font, width=20)
submit.grid(row=4, column=2, padx=10, pady=10)


def login():
    username = username_str_var.get()
    password = password_str_var.get()
    print('用户名:\t', username)
    print('密  码:\t', password)
    return None


submit.config(command=login)  # 点击的时候,自动执行 command + ()
# 绑定事案件,没有按钮对象
root.mainloop()

"""
    md -> markdown
    
"""