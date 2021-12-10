import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title('04 记事本')
root.geometry("800x500+100+100")

"""创建菜单栏"""
menubar = tk.Menu(root, tearoff=False)
root.config(menu=menubar)

filename = ''


def open_file():
    '''打开一个文件'''
    global filename  # 在函数内部声明一下全局变量,就可以在其他函数使用
    filename = filedialog.askopenfilename()
    content = open(filename, mode='r', encoding='utf-8').read()
    # tk.Text 文本框对象
    # tk.END 文本的最后面进行插入
    textPad.insert(tk.END, content)


def save_as():
    global filename
    filename = filedialog.asksaveasfilename()
    text = textPad.get('0.0', tk.END)
    open(filename, mode='w', encoding='utf-8').write(text)
    print('保存成功')


def save():
    global filename
    # 保存到之前读取的文件
    # save 方法里面拿到 open_file 方法里面的 filename, 能做到吗 ?
    text = textPad.get('0.0', tk.END)
    open(filename, mode='w', encoding='utf-8').write(text)


"""创建二级菜单 文件"""
file_menu = tk.Menu(menubar, tearoff=False)
file_menu.add_command(label='新建')
file_menu.add_command(label='打开', command=open_file)
file_menu.add_command(label='保存', command=save)
file_menu.add_command(label='另存为', command=save_as)
# 设置二级菜单的名字
menubar.add_cascade(label='文件', menu=file_menu)

"""创建二级菜单 编辑"""
edit_menu = tk.Menu(menubar, tearoff=False)
edit_menu.add_command(label='撤销')
edit_menu.add_command(label='重做')
# 添加分割线
edit_menu.add_separator()
edit_menu.add_command(label="复制")
edit_menu.add_command(label="剪切")
edit_menu.add_command(label="粘贴")
menubar.add_cascade(label="编辑", menu=edit_menu)


def author():
    pass


def about():
    pass


"""创建二级菜单 关于"""
about_menu = tk.Menu(menubar, tearoff=False)
about_menu.add_command(label="作者", command=author)
about_menu.add_command(label="版权", command=about)
menubar.add_cascade(label="关于", menu=about_menu)

var_status = tk.StringVar()
var_format = "字符数：{}"
var_status.set(var_format.format(0))
# 状态栏
status = tk.Label(root, textvariable=var_status, bd=1, relief=tk.SUNKEN, anchor=tk.W)
status.pack(side=tk.BOTTOM, fill=tk.X)
var_line = tk.StringVar()
# 行数
line_label = tk.Label(root, width=2, bg='antique white', textvariable=var_line, anchor=tk.N, font=('宋体', 24))
line_label.pack(side=tk.LEFT, fill=tk.Y)

# 文本编辑区域
textPad = tk.Text(root, undo=True, font=('宋体', 24))
textPad.pack(expand=tk.YES, fill=tk.BOTH)


def callback(event):
    print(event)
    text: str = textPad.get('0.0', tk.END)
    length = len(text.replace('\n', '').replace(' ', ''))
    var_status.set(var_format.format(length))

    line = len(text.split('\n')) - 1
    # 3 1 2 3
    line_str = ''
    for i in range(1, line + 1):
        line_str += str(i) + '\n'
    var_line.set(line_str)


textPad.bind('<Key>', callback)
# 滑动栏
scroll = tk.Scrollbar(textPad, cursor="circle")
textPad.config(yscrollcommand=scroll.set)
scroll.config(command=textPad.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

root.mainloop()
