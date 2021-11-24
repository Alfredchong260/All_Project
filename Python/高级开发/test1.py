from tkinter import *

root = Tk()
root.geometry("500x300+100+100")


def callback():
    print("新建文件")

menubar = Menu(root)
filemenu = Menu(menubar)

# 创建一个顶级菜单
menubar.add_cascade(label="文件", command=callback, menu=filemenu)
menubar.add_command(label="编辑", command=lambda: print('开始编辑'))
menubar.add_command(label="视图", command=lambda: print('视图'))
menubar.add_command(label="退出", command=root.quit)

filemenu.add_command(label='新建项目', command=lambda:print('文件 新建项目'))
filemenu.add_separator()
filemenu.add_command(label='打开', command=lambda:print('文件 打开本地文件'))

edit_menu = Menu(menubar,tearoff=False)

# 显示菜单
root.config(menu=menubar)
root.mainloop()
