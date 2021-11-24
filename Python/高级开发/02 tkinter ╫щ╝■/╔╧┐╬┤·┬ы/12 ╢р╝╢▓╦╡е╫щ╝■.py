import tkinter as tk

root = tk.Tk()
root.geometry('500x300+100+100')
font = ('宋体', 16)
# 1. 创建 1级菜单组件
menu_bar = tk.Menu(root)

# 2. 由一级菜单创建二级菜单
# tearoff=False 取消撕裂线
file_menu = tk.Menu(menu_bar, tearoff=False)
file_menu.add_command(label='新建项目', command=lambda: print('文件 新建项目'))
file_menu.add_separator()  # 手动加分割线
file_menu.add_command(label='打开', command=lambda: print('文件 打开本地文件'))
# 3. 将二级菜单绑定到一级菜单
menu_bar.add_cascade(label='文件', menu=file_menu)

edit_menu = tk.Menu(menu_bar, tearoff=False)
edit_menu.add_command(label='剪切', command=lambda: print('剪切'))
edit_menu.add_command(label='复制', command=lambda: print('复制'))
edit_menu.add_command(label='粘贴', command=lambda: print('粘贴'))
menu_bar.add_cascade(label='编辑', menu=edit_menu)
# 4. 给 root 对象绑定一级菜单
root.config(menu=menu_bar)

root.mainloop()
