import tkinter as tk

root = tk.Tk()
root.geometry('500x300+100+100')
# pack 顺序布局
# side 可以指定元素在页面中显示的位置(上下左右)
tk.Button(root, text='上 top').pack(side=tk.TOP)
tk.Button(root, text='下 Bottom').pack(side=tk.BOTTOM)
tk.Button(root, text='左 LEFT').pack(side=tk.LEFT)
tk.Button(root, text='右 Right').pack(side=tk.RIGHT)
tk.Button(root, text='下2 Bottom').pack(side=tk.BOTTOM)
tk.Button(root, text='下3 Bottom').pack(side=tk.BOTTOM)
root.mainloop()
