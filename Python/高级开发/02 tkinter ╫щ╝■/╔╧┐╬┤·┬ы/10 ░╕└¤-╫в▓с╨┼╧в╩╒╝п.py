import tkinter as tk

root = tk.Tk()
root.geometry('500x700+100+100')
font = ('宋体', 16)

username_str_var = tk.StringVar()
password_str_var = tk.StringVar()
password2_str_var = tk.StringVar()

tk.Label(root, width=8, height=2, text='', font=font).grid(row=0, column=0, sticky=tk.W)

tk.Label(root, text='用户名:', font=font).grid(row=1, column=1, sticky=tk.W)
tk.Entry(root, textvariable=username_str_var, font=font).grid(row=1, column=2, sticky=tk.W)

tk.Label(root, text='密 码:', font=font).grid(row=2, column=1, sticky=tk.W)
tk.Entry(root, textvariable=password_str_var, font=font).grid(row=2, column=2, sticky=tk.W)

tk.Label(root, text='确认密码:', font=font).grid(row=3, column=1, sticky=tk.W)
tk.Entry(root, textvariable=password2_str_var, font=font).grid(row=3, column=2, sticky=tk.W)

gender_list = ['保密', '男', '女']
gender_str_var = tk.StringVar()
gender_str_var.set('保密')

tk.Label(root, text='性别:', font=font).grid(row=4, column=1, sticky=tk.W)
tk.Radiobutton(root, variable=gender_str_var, font=font, value=gender_list[0], text=gender_list[0]
               ).grid(row=4, column=2, sticky=tk.W)

tk.Radiobutton(root, variable=gender_str_var, font=font, value=gender_list[1], text=gender_list[1]
               ).grid(row=5, column=1, sticky=tk.W)
tk.Radiobutton(root, variable=gender_str_var, font=font, value=gender_list[2], text=gender_list[2]
               ).grid(row=5, column=2, sticky=tk.W)

hobby_list = ['吃', '喝', '玩', '乐']
hobby_list_bool_var = [tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()]

tk.Label(root, text='兴趣爱好:', font=font).grid(row=6, column=1, sticky=tk.W)
tk.Checkbutton(root,
               variable=hobby_list_bool_var[0],
               font=font,
               text=hobby_list[0]
               ).grid(row=7, column=1, sticky=tk.W)
tk.Checkbutton(root,
               variable=hobby_list_bool_var[1],
               font=font,
               text=hobby_list[1]
               ).grid(row=7, column=2, sticky=tk.W)

tk.Checkbutton(root,
               variable=hobby_list_bool_var[2],
               font=font,
               text=hobby_list[2]
               ).grid(row=8, column=1, sticky=tk.W)
tk.Checkbutton(root,
               variable=hobby_list_bool_var[3],
               font=font,
               text=hobby_list[3]
               ).grid(row=8, column=2, sticky=tk.W)

button = tk.Button(root, width=20, text='确定', font=font)
button.grid(row=9, column=2, sticky=tk.W)


def click():
    print('获取参数')


button.config(command=click)
root.mainloop()
