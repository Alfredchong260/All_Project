""""""
"""
    注意！！！ -->  没有用到的组件可以用 entry 或者 button 组件代替, 或者是参考 Combobox `下拉选项卡.py` 里面的案例

    作业需求：参考 `网络调试工具.png` 完成页面的布局（实现页面布局即可）
"""
from tkinter import *
from tkinter import ttk

root = Tk()
root.title('网络调试工具')
root.geometry('1200x800')

# 先设置所有的框架
top_frame = Frame(root, width=1200, height=500, bg='blue')
top_frame.pack()

bottom_frame = Frame(root, width=1200, height=300, bg='red')
bottom_frame.pack()

top_left_frame = Frame(top_frame, width=200, height=300)
top_left_frame.pack(side=LEFT)
top_right_frame = Frame(top_frame, width=200, height=300)
top_right_frame.pack(side=RIGHT)

bottom_left_frame = Frame(bottom_frame, width=300, height=100, bg='blue')
bottom_left_frame.pack(side=LEFT, anchor=W)
bottom_right_frame = Frame(bottom_frame, width=860, height=100, bg='yellow')
bottom_right_frame.pack(side=RIGHT)

frame_font = ('', 18)
network = LabelFrame(top_left_frame, text='网络设置', width=200,
                     height=220, bd=2, font=frame_font)
network.pack(side=TOP, anchor=N)

receive = LabelFrame(top_left_frame, text='接收设置', width=200,
                     height=200, bd=2, font=frame_font)
receive.pack(side=TOP, anchor=N)

send = LabelFrame(bottom_left_frame, text='发送设置', width=200,
                  height=180, bd=2, font=frame_font)
send.pack(side=LEFT, anchor=N)



# 完成网络设置下的东西
network_font = ('', 16)
network_var = StringVar()
network_var1 = StringVar()
network_var2 = StringVar()
network_var2.set('7788')

Label(network, text='(1) 协议类型', font=network_font).pack(anchor=W)

choices = ('TCP 协议', 'UDP 协议', 'IP协议', 'FTP协议', 'Telnet协议', 'DNS协议')
dropbox = ttk.Combobox(
    network, width=20, textvariable=network_var, font=network_font, values=choices)
dropbox.current(0)
dropbox.pack(padx=10, pady=10)

Label(network, text='(2) 本地主机地址', font=network_font).pack(anchor=W)

choices1 = ('127.0.0.1',)
dropbox1 = ttk.Combobox(
    network, width=20, textvariable=network_var1, font=network_font, values=choices1)
dropbox1.current(0)
dropbox1.pack(padx=10, pady=10)

Label(network, text='(3) 本地端口', font=network_font).pack(anchor=W)
Entry(network, textvariable=network_var2, font=('', 15), width=22).pack()

Button(network, text='打开', font=network_font).pack()
Button(network, text='关闭', font=network_font).pack()

# 完成接收设置下的东西
receive_font = ('', 16)
radio_lst = ['UTF-8', 'GBK']
check_lst = ['json数据', '自动换行']
check_var_lst = [IntVar(), IntVar()]

radio_var = StringVar()
check_var = StringVar()
var = IntVar()

for index in range(len(radio_lst)):
    Radiobutton(receive, text=radio_lst[index], value=index,
                variable=var, font=receive_font, width=19).pack()

for index in range(len(check_lst)):
    Checkbutton(receive, text=check_lst[index],
                variable=check_var_lst[index], font=receive_font, width=17).pack()


# 完成发送设置下的东西
send_font = ('', 16)
send_radio_lst = ['UTF-8', 'GBK']
send_check_lst = ['数据加密(未实现)', '信息加密(未实现)']
send_check_var_lst = [IntVar(), IntVar()]

send_radio_var = StringVar()
send_check_var = StringVar()
send_var = IntVar()

for index in range(len(send_radio_lst)):
    Radiobutton(send, text=send_radio_lst[index], value=index,
                variable=send_var, font=send_font, width=19).pack()

for index in range(len(send_check_var_lst)):
    Checkbutton(send, text=send_check_lst[index],
                variable=send_check_var_lst[index], font=send_font, width=17).pack()

# 完成数据日志下的东西
Label(top_right_frame, text='数据日志', width=20, font=('', 15)).pack(side=TOP, anchor=W)
text1 = Text(top_right_frame, width=120, height=30, bd=2)
scrollbar = Scrollbar(top_right_frame, command=text1.yview, orient='vertical')
scrollbar.pack(side=RIGHT, fill=Y)
text1.pack(side=LEFT)
text1.configure(yscrollcommand=scrollbar.set)

# 完成信息发送下的东西
Label(bottom_right_frame, text='信息发送', width=78, font=('', 15)).pack(side=TOP, anchor=W)
# text2 = Text(bottom_right_frame, bd=2)
# text2.pack(side=RIGHT)

root.mainloop()
