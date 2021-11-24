from tkinter import *

root = Tk()
root.geometry('500x700')
font = ('', 18)

username_var = StringVar()
password_var = StringVar()
password_var2 = StringVar()

Label(root, width=8, height=2, text='').grid(row=0, column=0)

Label(root, width=8, text='用户名：', font=font).grid(row=1, column=1)
Entry(root, textvariable=username_var).grid(row=1, column=2)

Label(root, width=8, text='密 码：', font=font).grid(row=2, column=1)
Entry(root, textvariable=password_var).grid(row=2, column=2)

Label(root, width=8, text='确认密码：', font=font).grid(row=3, column=1)
Entry(root, textvariable=password_var2).grid(row=3, column=2)

gender_lst = ['保密', '男', '女']
gender_var = StringVar()

Label(root, width=8, text='性别：', font=font).grid(row=4, column=1)
Radiobutton(root, variable=gender_var, font=font,
            value=gender_lst[0], text=gender_lst[0]).grid(row=4, column=2)
Radiobutton(root, variable=gender_var, font=font,
            value=gender_lst[1], text=gender_lst[1]).grid(row=5, column=1)
Radiobutton(root, variable=gender_var, font=font,
            value=gender_lst[2], text=gender_lst[2]).grid(row=5, column=2)

Label(root, width=8, text='兴趣爱好：', font=font).grid(row=6, column=1)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()

Checkbutton(root, text='吃', variable=var1, font=font).grid(row=8, column=1)
Checkbutton(root, text='喝', variable=var2, font=font).grid(row=8, column=2)
Checkbutton(root, text='玩', variable=var3, font=font).grid(row=9, column=1)
Checkbutton(root, text='乐', variable=var4, font=font).grid(row=9, column=2)

root.mainloop()
