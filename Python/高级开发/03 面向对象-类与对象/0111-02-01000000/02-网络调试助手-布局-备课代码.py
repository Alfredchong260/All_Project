import socket
import tkinter as tk
from tkinter import ttk

WINDOW_SIZE = '650x500+50+50'

root = tk.Tk()
root.title('%s v%s' % ('网络调试助手', '0.0.1'))
root.geometry(WINDOW_SIZE)
# root.resizable(width=False, height=False)

"""左边布局"""
left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, anchor=tk.N, padx=5, pady=5)

"""左边布局 网络设置"""
network_frame = tk.LabelFrame(left_frame, text="网络设置", pady=5, padx=5)
network_frame.pack()

recv_mode = tk.IntVar()
recv_mode.set(0)
tk.Label(network_frame, text='(1) 协议类型').pack(anchor=tk.W)
agreement_type_variable = tk.StringVar()
agreement_type_variable.set("TCP 服务器")
w = ttk.Combobox(network_frame)
w['values'] = (agreement_type_variable.get(), "TCP 服务器", "TCP 客户端", "UDP")
w.current(0)
w.pack(fill=tk.X)

tk.Label(network_frame, text='(2) 本地主机地址').pack(anchor=tk.W)

host_variable = tk.StringVar()
host_variable.set("127.0.01")

hosts_list = ['134.175.188.27', '127.0.0.1']

host = ttk.Combobox(network_frame)
host['value'] = host_variable.get(), *hosts_list
host.current(0)
host.pack(fill=tk.X)

tk.Label(network_frame, text='(3) 本地端口').pack(anchor=tk.W)
port = tk.Entry(network_frame)
port.pack()

"""左边布局 网络设置 button按钮布局"""
button_frame = tk.Frame(network_frame)
button_frame.pack()

connect_button_open = tk.Button(button_frame, text='打开')
connect_button_open.pack(side=tk.LEFT)
connect_button_close = tk.Button(button_frame, text='关闭')
connect_button_close.pack()

"""左边布局 接收数据布局 """
recv_setting_frame = tk.LabelFrame(left_frame, text="接收设置", pady=5, padx=5)
recv_setting_frame.pack(side=tk.TOP, anchor=tk.N, fill=tk.X)

recv_hex_var = tk.IntVar()
tk.Radiobutton(recv_setting_frame, text="ASCII", variable=recv_hex_var, value=1).pack(anchor=tk.W)
tk.Radiobutton(recv_setting_frame, text="HEX", variable=recv_hex_var, value=2).pack(anchor=tk.W)

recv_v_int = [tk.IntVar(), tk.IntVar()]
# 提前选择内容
# v[3].set(1)
tk.Checkbutton(recv_setting_frame, text='按日志模式显示', variable=recv_v_int[0]).pack(anchor='w')
tk.Checkbutton(recv_setting_frame, text='接收完自动换行', variable=recv_v_int[1]).pack(anchor='w')

"""左边布局 发送数据"""
send_setting_frame = tk.LabelFrame(left_frame, text="发送设置", pady=5, padx=5)
send_setting_frame.pack(anchor=tk.N, fill=tk.X)

send_hex_var = tk.IntVar()
tk.Radiobutton(send_setting_frame, text="ASCII", variable=send_hex_var, value=1).pack(anchor=tk.W)
tk.Radiobutton(send_setting_frame, text="HEX", variable=send_hex_var, value=2).pack(anchor=tk.W)

send_v_int = [tk.IntVar(), tk.IntVar()]
# 提前选择内容
# v[3].set(1)
tk.Checkbutton(send_setting_frame, text='解析转义字符串', variable=send_v_int[0]).pack(anchor='w')
tk.Checkbutton(send_setting_frame, text='自动发送校验码', variable=send_v_int[1]).pack(anchor='w')

"""右边布局 """
right_frame = tk.Frame(root)
right_frame.pack(side=tk.TOP, padx=5, pady=5)

info_frame = tk.Frame(right_frame)
info_frame.pack()

tk.Label(info_frame, text="数据日志").pack()
text_area = tk.Text(info_frame, width=62)
text_area.pack(side=tk.LEFT, fill=tk.X)
send_scr_bar = tk.Scrollbar(info_frame)
send_scr_bar.pack(side=tk.RIGHT, fill=tk.Y)
# 设置 text_area 的 y 坐标为滚动条
text_area.config(yscrollcommand=send_scr_bar.set)
# 设置滚动条的命令为 text_area 的 y 视图
send_scr_bar.config(command=text_area.yview)

tk.Label(right_frame, text="信息发送").pack(anchor=tk.W)

"""右边布局 发送框与信息"""
send_frame = tk.Frame(right_frame)
send_frame.pack(side=tk.LEFT, fill=tk.X)

send_area = tk.Text(send_frame, width=58, height=6)
send_area.pack(side=tk.LEFT)

send_button = tk.Button(send_frame, text='发送', width=4)
send_button.pack(side=tk.LEFT, fill=tk.Y)


root.mainloop()
