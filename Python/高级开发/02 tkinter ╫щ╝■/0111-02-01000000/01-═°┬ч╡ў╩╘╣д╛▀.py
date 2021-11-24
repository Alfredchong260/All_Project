""""""
"""
    注意！！！ -->  没有用到的组件可以用 entry 或者 button 组件代替, 或者是参考 Combobox `下拉选项卡.py` 里面的案例

    作业需求：参考 `网络调试工具.png` 完成页面的布局（实现页面布局即可）
"""
from tkinter import *
from tkinter import ttk

root = Tk()
root.title('网络调试工具')
root.geometry('650x530')

# 先设置所有的框架
left_frame = Frame(root)
left_frame.pack(side=LEFT, anchor=N)

network = LabelFrame(left_frame, text='网络设置')
network.pack(side=TOP, padx=5, pady=5)

receive = LabelFrame(left_frame, text='接收设置')
receive.pack(side=TOP, padx=5, pady=5)

send = LabelFrame(left_frame, text='发送设置')
send.pack(side=TOP, padx=5, pady=5)

# 完成网络设置下的东西
network_var = StringVar()
network_entry_var = StringVar()
network_entry_var.set('7788')

choices = ('TCP 协议', 'UDP 协议', 'IP协议', 'FTP协议', 'Telnet协议', 'DNS协议')

Label(network, text='(1) 协议类型').pack(anchor=W)

combo = ttk.Combobox(network, textvariable=network_var, values=choices)
combo.pack(anchor=W)
combo.current(0)

Label(network, text='(2) 本地主机地址').pack(anchor=W)

choices1 = ('127.0.0.1',)
combo1 = ttk.Combobox(network, textvariable=network_var, values=choices1)
combo1.pack(anchor=W)
combo1.current(0)

Label(network, text='(3) 本地端口').pack(anchor=W)
Entry(network, textvariable=network_entry_var).pack()

btn_frame = Frame(network)
btn_frame.pack()

Button(btn_frame, text='打开').pack(side=LEFT)
Button(btn_frame, text='关闭').pack(side=LEFT)

# 完成接收设置下的东西
radio_lst = ['UTF-8', 'GBK']
check_lst = ['json数据', '自动换行']
check_var_lst = [IntVar(), IntVar()]

radio_var = StringVar()
check_var = StringVar()
var = IntVar()

for index in range(len(radio_lst)):
    Radiobutton(send, text=radio_lst[index], value=index,
                variable=var, width=18).pack()

for index in range(len(check_lst)):
    Checkbutton(send, text=check_lst[index],
                variable=check_var_lst[index]).pack()

# 完成发送设置下的东西
radio_lst = ['UTF-8', 'GBK']
check_lst = ['数据加密(未实现)', '信息接收(未实现)']
check_var_lst = [IntVar(), IntVar()]

radio_var = StringVar()
check_var = StringVar()
var = IntVar()

for index in range(len(radio_lst)):
    Radiobutton(receive, text=radio_lst[index], value=index,
                variable=var, width=18).pack()

for index in range(len(check_lst)):
    Checkbutton(receive, text=check_lst[index],
                variable=check_var_lst[index]).pack()

# 完成数据日志下的东西
right_frame = Frame(root)
right_frame.pack(side=LEFT)

Label(right_frame, text='数据日志', font=('', 12)).pack(anchor=W)
Text(right_frame, width=68).pack(anchor=W)
Label(right_frame, text='信息发送', font=('', 12)).pack(anchor=W)
# 完成信息发送下的东西

send_frame = Frame(right_frame)
send_frame.pack()

send_text = Text(send_frame, height=5, width=60)
send_text.pack(side=LEFT)

Button(send_frame, text='发送', height=5).pack(side=LEFT)

root.mainloop()
