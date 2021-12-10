"""
    将登录页面抽象为登录对象

        属性: 标题,宽高,位置....
        行为: 创建页面的的组件, 登录按钮点击事件/(校验输入的信息时候正确)
"""

import tkinter as tk


class MainPage:
    def __init__(self, master, size='800x500'):
        # 2. 创建root 对象与初始化一些属性
        self.root = master
        self.root.geometry(size)
        self.font = ('宋体', 18)
        # 在第二个页面重新绘制


class LoginPage:
    def __init__(self, main_root, size='500x300+100+100'):
        # 2. 创建root 对象与初始化一些属性
        self.root = main_root
        self.root.geometry(size)
        self.font = ('宋体', 18)
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.username_str_var = tk.StringVar()
        self.password_str_var = tk.StringVar()

        # 3. 创建页面上的元素
        self.create_page()  # 创建页面上的元素
        # 在 init 里面显示界面 ?
        # self.root.mainloop()

    def create_page(self):
        tk.Label(self.frame, text='', font=self.font, width=5, height=3).grid(row=0, column=0)
        tk.Label(self.frame, text='用户名:', font=self.font).grid(row=1, column=1, padx=10, pady=10)
        tk.Entry(self.frame, font=self.font, textvariable=self.username_str_var).grid(row=1, column=2, padx=10, pady=10)
        tk.Label(self.frame, text='密 码:', font=self.font).grid(row=2, column=1, padx=10, pady=10)
        tk.Entry(self.frame, font=self.font, textvariable=self.password_str_var).grid(row=2, column=2, padx=10, pady=10)

        # 没有第三行,后面的就会上移
        self.submit = tk.Button(self.frame, text='提交', font=self.font, width=20)
        self.submit.grid(row=4, column=2, padx=10, pady=10)
        # 3. 然后绑定登录事件
        self.submit.config(command=self.login)

    def login(self):
        username = self.username_str_var.get()
        password = self.password_str_var.get()
        print('用户名:\t', username)
        print('密  码:\t', password)
        self.frame.destroy()  # 销毁布局组件
        MainPage(self.root)


main_root = tk.Tk()
# 1. 创建实例对象的是会调用初始化方法
login_page = LoginPage(main_root, '500x300')
# # 5. 显示页面
# 对于代码的逻辑是没有区别的
# login_page.root.mainloop()
main_root.mainloop()
