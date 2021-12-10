""""""

"""
    注意！！！ -->  没有用到的组件可以用 entry 或者 button 组件代替,
     或者是参考 Combobox `下拉选项卡.py` 里面的案例

    作业需求：参考 `网络调试工具.png` 完成页面的布局（实现页面布局即可）
"""
import tkinter as tk
from tkinter import ttk  # tkinter 的增强版,可以定制一些样式

root = tk.Tk()
root.geometry('650x530')
"""左边的布局"""
left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, anchor=tk.N)

"""左边的布局 网络设置布局"""
net_frame = tk.LabelFrame(left_frame, text='网络设置')
net_frame.pack(side=tk.TOP)
tk.Label(net_frame, text='(1)协议类型').pack(anchor=tk.W)

# 创建一个下拉列表
server_type_str_var = tk.StringVar()
server_select = ttk.Combobox(net_frame, width=12, textvariable=server_type_str_var)
server_select.pack(anchor=tk.W)
# 设置下拉列表的值
server_select['values'] = ('TCP服务器', 2, 4, 42, 100)
server_select.current(0)
tk.Label(net_frame, text='(2)本地主机地址').pack(anchor=tk.W)
server_select2 = ttk.Combobox(net_frame, width=12, textvariable=server_type_str_var)
server_select2.pack(anchor=tk.W)
# 设置下拉列表的值
server_select2['values'] = ('127.0.0.1', 2, 4, 42, 100)
server_select2.current(0)
tk.Label(net_frame, text='(3)本地端口').pack(anchor=tk.W)
tk.Entry(net_frame).pack(anchor=tk.W)

button_frame = tk.Frame(net_frame)
button_frame.pack()

tk.Button(button_frame, text='打开').pack(side=tk.LEFT)
tk.Button(button_frame, text='关闭').pack(side=tk.LEFT)
"""左边的布局 接受设置布局"""
"""左边的布局 发送设置布局"""

# 右边的布局
right_frame = tk.Frame(root)
right_frame.pack(side=tk.LEFT, anchor=tk.N)

tk.Label(right_frame, text='数据日志').pack(anchor=tk.W)
tk.Text(right_frame).pack(anchor=tk.W)
tk.Label(right_frame, text='信息发送').pack(anchor=tk.W)

send_frame = tk.Frame(right_frame)
send_frame.pack()

send_text = tk.Text(send_frame, height=5, width=65)
send_text.pack(side=tk.LEFT)
tk.Button(send_frame, text='发送', height=5).pack(side=tk.LEFT)

root.mainloop()
