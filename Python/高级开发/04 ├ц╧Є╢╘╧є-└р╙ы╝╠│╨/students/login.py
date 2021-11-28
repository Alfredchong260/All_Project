import tkinter as tk
import tkinter.messagebox


class MainPage:
    """登录成功之后的 tk.Tk 对象"""

    def __init__(self, master):
        # 第二个页面
        self.root = master
        # 1. 重新设置窗口的大小
        self.root.geometry('500x300')
        # 2. 需要菜单栏，当点击不同的菜单之后，需要实现显示内容的切换


class LoginPage:  # tk.Frame
    """登录时候的窗口对象"""

    def __init__(self, master):
        # 2.1 拿到窗口对象，给窗口对象设置一些基本的属性
        self.root = master
        self.root.geometry('300x180')

        # 2.2 创建登录页面需要用到的可变百年来
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        # 2.3 创建一个登录页面的内容布局 （布局可以销毁、隐藏、重新创建）
        self.page = tk.Frame(self.root)  # 创建 Frame
        self.page.pack()

        # 2.4 调用创建页面方法
        self.create_page()

    def create_page(self):
        # 2.4.1 绘制内容
        tk.Label(self.page).grid(row=0, column=0)

        tk.Label(self.page, text='账户: ').grid(row=1, column=0)
        tk.Entry(self.page, textvariable=self.username).grid(row=1, column=1)

        tk.Entry(self.page, textvariable=self.password).grid(row=2, column=1)
        tk.Label(self.page, text='密码: ').grid(row=2, column=0)
        # 2.4.2 当登录按钮点击之后触发 self.login_check
        tk.Button(self.page, text='登陆', command=self.login_check).grid(row=3, pady=10)
        # 当退出按钮点击之后触发 self.page.quit
        tk.Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=1)  # quit 退出整个程序

    def login_check(self):
        """登录检测"""
        ## 1. 获取页面输入的参数
        name = self.username.get()
        secret = self.password.get()
        ## 2. 校验参数是否正确
        if name == 'admin' and secret == '123456':
            ## 3. 如果参数正确，就销毁 frame
            self.page.destroy()  # frame 组件的一个方法,可以销毁 tk.Frame
            # 4. 将窗口对象传递给 MainPage 触发 MainPage 的 __init__ 方法
            MainPage(self.root)
        else:
            tkinter.messagebox.showinfo(title='错误', message='账号或密码错误！')


"""
    程序执行的顺序是逻辑顺序
    
    窗口对象是本子 
    
    Frame 布局是一张纸
    
    本子可以翻页
"""
# 1. 创建一个窗口对象
root = tk.Tk()
# 2. 将窗口对象传递给封装好的登录页面
LoginPage(root)
# 3. 显示窗口对象
root.mainloop()


