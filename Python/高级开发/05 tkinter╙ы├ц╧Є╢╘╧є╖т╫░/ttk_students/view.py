import tkinter as tk
from tkinter import ttk

from db import db


class AddFrame(tk.Frame):
    """新增页面的布局"""

    def __init__(self, master):
        super(AddFrame, self).__init__(master)
        self.name = tk.StringVar()
        self.math = tk.StringVar()
        self.chinese = tk.StringVar()
        self.english = tk.StringVar()
        self.status = tk.StringVar()
        self.create_page()

    def create_page(self):
        # stick 控件对象方向 tk.W 西方位
        # pady padding y 上下的宽度
        # row 行 表格布局
        tk.Label(self).grid(row=0, stick=tk.W, pady=10)
        tk.Label(self, text='姓 名: ').grid(row=1, stick=tk.W, pady=10)
        # text variable 绑定控件里面的数据内容
        tk.Entry(self, textvariable=self.name).grid(row=1, column=1, stick=tk.E)
        tk.Label(self, text='数 学: ').grid(row=2, stick=tk.W, pady=10)
        tk.Entry(self, textvariable=self.math).grid(row=2, column=1, stick=tk.E)
        tk.Label(self, text='语 文: ').grid(row=3, stick=tk.W, pady=10)
        tk.Entry(self, textvariable=self.chinese).grid(row=3, column=1, stick=tk.E)
        tk.Label(self, text='英 语: ').grid(row=4, stick=tk.W, pady=10)
        tk.Entry(self, textvariable=self.english).grid(row=4, column=1, stick=tk.E)
        tk.Button(self, text='录入', command=self.recode_student).grid(row=5, column=1, stick=tk.E, pady=10)
        tk.Label(self, textvariable=self.status).grid(row=6, column=1, stick=tk.E, pady=10)

    def recode_student(self):
        """记录学生的信息"""
        # 1. 拿到学生的信息,将信息存到数数据模型
        stu = {
            "name": self.name.get(),
            "math": self.math.get(),
            "chinese": self.chinese.get(),
            "english": self.english.get()
        }
        print('stu:\t', stu)
        db.insert(student=stu)
        print(db.all())
        self.status.set('插入数据成功')
        # db.save_data()


class SearchFrame(tk.Frame):
    """新增页面的布局"""

    def __init__(self, master):
        super(SearchFrame, self).__init__(master)
        self.itemName = tk.StringVar()

        self.table_frame = tk.Frame(self)

        search_form_frame = tk.Frame(self.table_frame)
        self.table_frame.pack()
        # 查询表单
        search_form_frame.pack()
        tk.Label(search_form_frame, text='请输入姓名:').pack(side=tk.LEFT)
        tk.Entry(search_form_frame).pack(side=tk.LEFT)
        tk.Button(search_form_frame, text='查询').pack(side=tk.LEFT)

        self.row = 1

        self.create_page()

    def create_page(self):
        self.create_tree_view()
        self.show_data_frame()
        tk.Button(self, text='刷新数据', command=self.show_data_frame).pack(anchor=tk.E, pady=5)

    def show_data_frame(self):
        # 1. 删除原节点 没有办法做到动态更新数据
        for _ in map(self.tree_view.delete, self.tree_view.get_children("")):
            pass
        # 2. 获取所有数据
        students = db.all()
        # 3. 插入数据到页面
        for index, stu in enumerate(students):
            print(stu)
            self.tree_view.insert('', index + 1,
                                  values=(stu['name'], str(stu['chinese']), str(stu['math']), str(stu['english'])))

    def create_tree_view(self):
        # 表格
        columns = ("name", "chinese", "math", "english")
        columns_value = ('姓名', '语文', '数学', '英语')
        self.tree_view = ttk.Treeview(self, show="headings", columns=columns)
        self.tree_view.column('name', width=80, anchor='center')
        self.tree_view.column('chinese', width=80, anchor='center')
        self.tree_view.column('math', width=80, anchor='center')
        self.tree_view.column('english', width=80, anchor='center')
        self.tree_view.heading('name', text='姓名')
        self.tree_view.heading('chinese', text='语文')
        self.tree_view.heading('math', text='数学')
        self.tree_view.heading('english', text='英语')
        self.tree_view.pack(fill=tk.BOTH, expand=True)


class ChangeFrame(tk.Frame):
    """修改数据页面的布局"""

    def __init__(self, master):
        super(ChangeFrame, self).__init__(master)
        tk.Label(self, text='修改界面').pack()
        self.change_frame = tk.Frame(self)
        self.change_frame.pack()
        self.status = tk.StringVar()
        self.name = tk.StringVar()
        self.math = tk.StringVar()
        self.chinese = tk.StringVar()
        self.english = tk.StringVar()

        self.create_page()

    def create_page(self):
        tk.Label(self.change_frame).grid(row=0, stick=tk.W, pady=1)
        tk.Label(self.change_frame, text='姓 名: ').grid(row=1, stick=tk.W, pady=10)
        tk.Entry(self.change_frame, textvariable=self.name).grid(row=1, column=1, stick=tk.E)
        tk.Label(self.change_frame, text='数 学: ').grid(row=2, stick=tk.W, pady=10)
        tk.Entry(self.change_frame, textvariable=self.math).grid(row=2, column=1, stick=tk.E)
        tk.Label(self.change_frame, text='语 文: ').grid(row=3, stick=tk.W, pady=10)
        tk.Entry(self.change_frame, textvariable=self.chinese).grid(row=3, column=1, stick=tk.E)
        tk.Label(self.change_frame, text='英 语: ').grid(row=4, stick=tk.W, pady=10)
        tk.Entry(self.change_frame, textvariable=self.english).grid(row=4, column=1, stick=tk.E)
        tk.Button(self.change_frame, text='查询', command=self._search).grid(row=6, column=0, stick=tk.W, pady=10)
        tk.Button(self.change_frame, text='修改', command=self._change).grid(row=6, column=1, stick=tk.E, pady=10)
        tk.Label(self.change_frame, textvariable=self.status).grid(row=7, column=1, stick=tk.E, pady=10)

    def _search(self):
        # 查询到了才能修改
        name = self.name.get()
        stu = db.search_by_name(name)
        if stu:
            self.chinese.set(stu['chinese'])
            self.math.set(stu['math'])
            self.english.set(stu['english'])
            self.status.set('数据查询成功')
        else:
            self.chinese.set('')
            self.math.set('')
            self.english.set('')
            self.status.set('数据查询失败')

    def _change(self):
        # 修改之后要保存数据
        # 1. 拿到学生的信息,将信息在数数据模型中修改
        stu = {
            "name": self.name.get(),
            "math": self.math.get(),
            "chinese": self.chinese.get(),
            "english": self.english.get()
        }
        flag = db.update(stu)
        if flag:
            self.status.set('数据修改成功')
            self.chinese.set('')
            self.math.set('')
            self.english.set('')
            self.name.set('')
        else:
            self.status.set('数据修改失败,请检查名字是否正确')


class AboutFrame(tk.Frame):
    """修改数据页面的布局"""

    def __init__(self, master):
        super(AboutFrame, self).__init__(master)
        tk.Label(self, text='关于页面').pack()
        tk.Label(self, text='作者信息: 青灯教育-正心老师').pack()
        tk.Label(self, text='版权所有: 青灯教育').pack()
