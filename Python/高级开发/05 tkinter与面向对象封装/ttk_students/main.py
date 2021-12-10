import tkinter as tk
from view import AddFrame, AboutFrame, ChangeFrame, SearchFrame


class MainPage:
    def __init__(self, master):
        # 主页是最终的页面
        self.root: tk.Tk = master
        self.root.geometry('500x300+150+150')
        self.root.title('学生信息管理系统-主页面')

        self.create_page()

    def create_page(self):
        self.about_frame = AboutFrame(self.root)
        # tk.Label(self.about_frame, text='本项目有青灯教育-正心老师开发').pack()
        # about_frame.pack()

        self.change_frame = ChangeFrame(self.root)
        self.search_frame = SearchFrame(self.root)
        # tk.Label(self.change_frame, text='修改页面布局').pack()

        self.add_frame = AddFrame(self.root)  # tk.Frame(root)
        # tk.Label(self.add_frame, text='添加数据页面').pack()

        menubar = tk.Menu(self.root)
        menubar.add_command(label='录入', command=self.show_add_frame)
        menubar.add_command(label='查询', command=self.show_search_frame)
        menubar.add_command(label='删除')
        menubar.add_command(label='修改', command=self.show_change_frame)
        menubar.add_command(label='关于', command=self.show_about_frame)

        self.root['menu'] = menubar  # 设置菜单栏

    def show_about_frame(self):
        # pack 布局到页面
        self.about_frame.pack()
        # pack_forget 在页面上隐藏布局
        # destroy 直接从内存中销毁
        self.change_frame.pack_forget()
        self.add_frame.pack_forget()
        self.search_frame.pack_forget()

    def show_change_frame(self):
        self.change_frame.pack()
        self.about_frame.pack_forget()
        self.add_frame.pack_forget()
        self.search_frame.pack_forget()

    def show_add_frame(self):
        self.add_frame.pack()
        self.change_frame.pack_forget()
        self.about_frame.pack_forget()
        self.search_frame.pack_forget()

    def show_search_frame(self):
        self.search_frame.pack()
        self.about_frame.pack_forget()
        self.change_frame.pack_forget()
        self.add_frame.pack_forget()


root = tk.Tk()
MainPage(root)
root.mainloop()
