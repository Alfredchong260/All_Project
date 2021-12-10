import tkinter as tk

root = tk.Tk()
root.geometry('800x500+100+100')
font = ('宋体', 18)
# 上半部分
top_frame = tk.Frame(root)
top_frame.pack()
tk.Label(top_frame, text='怎么敲代码才不会报错?', font=('宋体', 32)).pack()

# 下半部分
bottom_frame = tk.Frame(root)
bottom_frame.pack()
# 左
bottom_left_frame = tk.Frame(bottom_frame)
bottom_left_frame.pack(side=tk.LEFT)

user_info_frame = tk.LabelFrame(bottom_left_frame, text='个人信息')
user_info_frame.pack()
radio_var_str = tk.StringVar()
tk.Label(user_info_frame, text='性别').pack()
tk.Radiobutton(user_info_frame, text='男', font=font, variable=radio_var_str, value='男').pack(anchor=tk.W)
tk.Radiobutton(user_info_frame, text='女', font=font, variable=radio_var_str, value='女').pack(anchor=tk.W)
tk.Radiobutton(user_info_frame, text='保密', font=font, variable=radio_var_str, value='其他').pack(anchor=tk.W)

hobby_frame = tk.LabelFrame(bottom_left_frame, text='个人信息')
hobby_frame.pack()

hobby_list = ['吃', '喝', '玩', '乐']
hobby_list_bool_var = [tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()]

tk.Label(hobby_frame, text='兴趣爱好:', font=font).pack()
tk.Checkbutton(hobby_frame, variable=hobby_list_bool_var[0], font=font, text=hobby_list[0]).pack()
tk.Checkbutton(hobby_frame, variable=hobby_list_bool_var[1], font=font, text=hobby_list[1]).pack()
tk.Checkbutton(hobby_frame, variable=hobby_list_bool_var[2], font=font, text=hobby_list[2]).pack()
tk.Checkbutton(hobby_frame, variable=hobby_list_bool_var[3], font=font, text=hobby_list[3]).pack()

# 右
bottom_right_frame = tk.Frame(bottom_frame)
bottom_right_frame.pack(side=tk.RIGHT)
province_frame = tk.Frame(bottom_right_frame)
province_frame.pack()
province_str_var = tk.StringVar()
province_str_var.set('辽宁省')
tk.Label(province_frame, text='所在省份').pack(side=tk.LEFT)
# text 显示到界面 --> GUI
# variable 可变变量,当单选框选中之后,会将value复制给 variable
# value
tk.Radiobutton(province_frame, text='辽宁省', font=font, variable=province_str_var, value='辽宁省').pack(side=tk.LEFT)
tk.Radiobutton(province_frame, text='北京', font=font, variable=province_str_var, value='北京').pack(side=tk.LEFT)
tk.Radiobutton(province_frame, text='上海', font=font, variable=province_str_var, value='上海').pack(side=tk.LEFT)

tk.Text(bottom_right_frame, ).pack()
tk.Button(bottom_right_frame, text='提交').pack()
root.mainloop()
