import tkinter as tk
from tkinter import messagebox
from main import MainPage  # 必须是在项目的根目录下才能这样导入


class LoginPage:
    def __init__(self, master):
        # 1.1 定义内部变量root
        self.root = master
        # 1.2 设置窗口大小
        self.root.geometry('300x180+150+150')
        self.root.title('学生信息管理系统-登录页')

        # 定义可以在页面更新数据的变量 普通字符串改变之后无法及时在页面中刷新
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        # 1.3 创建新的 布局控件 找一张新的纸作画 画 内容 需要画在纸上面
        self.page = tk.Frame(self.root)  # 创建Frame
        # 将控件布局到 root 对象 （GUI 程序对象）
        self.page.pack()
        self.creat_page()

    def login_check(self):
        """登录检测"""
        name = self.username.get()
        secret = self.password.get()
        if name == 'admin' and secret == '123456':
            self.page.destroy()
            MainPage(root)
        else:
            messagebox.showinfo(title='错误', message='账号或密码错误！')

    def creat_page(self):
        # 1.4 绘制内容
        tk.Label(self.page).grid(row=0, column=0)

        tk.Label(self.page, text='账户: ').grid(row=1, column=0)
        tk.Entry(self.page, textvariable=self.username).grid(row=1, column=1)

        tk.Entry(self.page, textvariable=self.password).grid(row=2, column=1)
        tk.Label(self.page, text='密码: ').grid(row=2, column=0)

        tk.Button(self.page, text='登陆', command=self.login_check).grid(row=3, pady=10)
        tk.Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=1)


root = tk.Tk()
LoginPage(root)
root.mainloop()
