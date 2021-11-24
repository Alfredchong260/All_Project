import tkinter as tk

root = tk.Tk()
root.geometry('500x300+100+100')
font = ('宋体', 16)
# 1. 创建菜单组件
menu_bar = tk.Menu(root)


def func():
    print('文件按钮被点击了')


func2 = lambda: print('编辑按钮被点击了')

# 2. 给菜单组件添加选项
menu_bar.add_command(label='文件', command=func)
menu_bar.add_command(label='编辑', command=func2)
menu_bar.add_command(label='视图', command=lambda: print('视图按钮被点击了'))

# 3. 给 root 对象绑定菜单
root.config(menu=menu_bar)

root.mainloop()
