import tkinter as tk

root = tk.Tk()
root.geometry('500x300+100+100')
# pack 顺序布局 默认的情况下只能在一个方向进行布局
# 默认是从上到下

tk.Label(root, text='用户名:').pack(side=tk.LEFT)
tk.Entry(root).pack(side=tk.LEFT)
tk.Label(root, text='密码:').pack(side=tk.LEFT)
tk.Entry(root).pack(side=tk.LEFT)
tk.Button(root, text='提交').pack(side=tk.LEFT)
root.mainloop()
