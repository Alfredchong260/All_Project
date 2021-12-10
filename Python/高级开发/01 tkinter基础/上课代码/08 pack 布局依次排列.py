import tkinter as tk

root = tk.Tk()
root.geometry('500x300+100+100')
# pack 顺序布局
# 默认是从上到下
tk.Button(root, bg='red', width=5).pack(side=tk.TOP)
tk.Button(root, bg='yellow', width=5).pack(side=tk.TOP)
tk.Button(root, bg='blue', width=5).pack(side=tk.TOP)

# left 左
tk.Button(root, bg='red', width=5).pack(side=tk.LEFT)
tk.Button(root, bg='yellow', width=5).pack(side=tk.LEFT)
tk.Button(root, bg='blue', width=5).pack(side=tk.LEFT)

# right 从右到左
tk.Button(root, bg='red', width=5).pack(side=tk.RIGHT)
tk.Button(root, bg='yellow', width=5).pack(side=tk.RIGHT)
tk.Button(root, bg='blue', width=5).pack(side=tk.RIGHT)
root.mainloop()
