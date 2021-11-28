"""
    创建一个窗口页面，需求如下
        标题为：青灯教育-学生信息管理系统
        位置：出现的位置为屏幕居中
        窗口大小为：500*300

    请将登录框封装为面向对象的结构
"""

import tkinter as tk


class LoginPage:
    def __init__(self, master):
        # 2.1 创建一个页面布局的内容
        self.root = master

        self.root.title('青灯教育-学生信息管理系统')

        self.screen_x = self.root.winfo_screenwidth()
        self.screen_y = self.root.winfo_screenheight()
        # 2.2 创建一个布局组件
        self.login_frame = tk.Frame()  # 页面布局组件
        self.login_frame.pack()

        self.root.geometry('500x300+{}+{}'.format(int(self.screen_x / 2 - 150), int(self.screen_y / 2 - 150)))
        # 2.3 调用创建布局的方法
        self.create_page()
        # self.root.mainloop()

    def create_page(self):
        # 2.4 往页面上布局元素
        label1 = tk.Label(self.login_frame, text='账号')
        label1.pack(side=tk.LEFT, anchor=tk.N)
        entry1 = tk.Entry(self.login_frame)
        entry1.pack(side=tk.LEFT, anchor=tk.N)

        label2 = tk.Label(self.login_frame, text='密码：')
        label2.pack(side=tk.LEFT, anchor=tk.N)
        entry2 = tk.Entry(self.login_frame)
        entry2.pack(side=tk.LEFT, anchor=tk.N)

        tk.Button(self.login_frame, text='提交').pack(side=tk.BOTTOM)

        menu = tk.Menu(self.root)
        menu.add_command(label='显示', command=self.login_frame.pack)
        menu.add_command(label='影藏', command=self.login_frame.forget)
        self.root.config(menu=menu)


# 1. 创建窗口对象
root = tk.Tk()
LoginPage(master=root)  # 2. LoginPage 创建一个实例对象
# 3. 进入事件循环,显示窗口
root.mainloop()
