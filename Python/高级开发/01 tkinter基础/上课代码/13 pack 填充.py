import tkinter as tk

root = tk.Tk()
root.geometry('500x300+100+100')
# pack 布局填充,上下布局左右填充
# fill  tk.X  tk.Y  tk.BOTH +
tk.Button(root, text='上 top', bg='red').pack(side=tk.TOP, fill=tk.X)
# 先被 bottom 给占位了
tk.Button(root, text='下 Bottom').pack(side=tk.BOTTOM)
#
tk.Button(root, text='左 LEFT').pack(side=tk.LEFT, fill=tk.Y)
tk.Button(root, text='右 Right', bg='#1d953f', font=('宋体', 18)).pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

root.mainloop()
