""""""
from tkinter import *
import tkinter as tk
import json

"""
    参考 `学生信息管理系统-数据修改.png` 实现学生信息管理系统的修改部分布局与逻辑代码
    
    首先输入名字，查询学生信息
        如果没有查询到信息，就显示此学生不存在
        查询到了信息，就将信息显示到页面上
    可以随意修改页面是显示的学生信息，修改完之后点击提交就能完成修改
"""


class MySqlDB:
    CLS_HOST = "127.0.0.1"

    def __init__(self):
        # [{}, {}, {}]
        # 初始化方法里面创建实例属性
        self.filename = 'students.json'
        self.students = []
        # 启动程序的时候就加载数据  创建对象的时候，加载数据
        self.load()

    def insert(self, student):
        """
        增加学员信息的方法
        :param student: 字典格式的学生信息
        :return:
        """
        self.students.append(student)

    def delete(self, student):
        """
        :param student: 字典格式的学生信息
        :return:
        """
        self.students.remove(student)

    def search(self, name):
        """
        指定姓名查询学生信息
        :param name: 学员姓名
        :return: 学员信息 or None
        """
        for stu in self.students:
            if stu['name'] == name:
                return stu
        return None

    def change(self, stu):
        """
        修改学员信息
        :param stu: 需要修改的学员信息
        :return: True or False
        """
        old_stu = self.search(stu['name'])
        if old_stu:
            index = self.students.index(old_stu)
            self.students[index].update(stu)
            return True
        else:
            return False

    def save(self):
        with open(self.filename, mode='w', encoding='utf-8') as f:
            data = json.dumps(self.students, ensure_ascii=False)
            f.write(data)

    def load(self):
        # 缺少文件的名字
        with open(self.filename, mode='r', encoding='utf-8') as f:
            data = f.read()
            self.students = json.loads(data)

    def all(self):
        return self.students

    @staticmethod
    def help():
        return "学生信息管理系统的数据操作类"


db = MySqlDB()


class ChangeFrame(tk.Frame, MySqlDB):  # 继承Frame类
    def __init__(self, master=None):
        super().__init__(master)

        self.students = json.loads(open('./students.json', 'r', encoding='utf-8').read())

        self.font = ('', 12)
        self.name = StringVar()
        self.math = StringVar()
        self.chinese = StringVar()
        self.english = StringVar()
        self.total = StringVar()

        self.create_page()

    def create_page(self):
        # 补全创建页面逻辑
        top = Frame(self.master)
        top.pack()

        middle = Frame(self.master)
        middle.pack()

        Label(top, text='修改界面', font=self.font).pack()
        self.label = Label(top, text='', font=self.font)
        self.label.pack()

        Label(middle, text='姓名:', font=self.font).grid(
            row=1, column=1, padx=10, pady=10)
        Entry(middle, font=self.font, textvariable=self.name).grid(
            row=1, column=2, padx=10, pady=10)
        Label(middle, text='数学:', font=self.font).grid(
            row=2, column=1, padx=10, pady=10)
        Entry(middle, font=self.font, textvariable=self.math).grid(
            row=2, column=2, padx=10, pady=10)
        Label(middle, text='语文:', font=self.font).grid(
            row=3, column=1, padx=10, pady=10)
        Entry(middle, font=self.font, textvariable=self.chinese).grid(
            row=3, column=2, padx=10, pady=10)
        Label(middle, text='英语:', font=self.font).grid(
            row=4, column=1, padx=10, pady=10)
        Entry(middle, font=self.font, textvariable=self.english).grid(
            row=4, column=2, padx=10, pady=10)

        Button(middle, text='查询', command=self._search).grid(row=5, column=1)
        Button(middle, text='修改', command=self._change).grid(
            row=5, column=2, sticky=E)

    def _search(self):
        # 补全查找逻辑
        try:
            self.label.config(text='')
            name = self.name.get()
            var = self.search(name)

            self.math.set(var['math'])
            self.chinese.set(var['chinese'])
            self.english.set(var['english'])
            self.total.set(var['total'])
        except Exception:
            self.label.config(text=f"{self.name.get()}不存在")

    def _change(self):
        # 补全修改数据逻辑
        try:
            self.label.config(text='')
            name = self.name.get()
            math = int(self.math.get())
            chinese = int(self.chinese.get())
            english = int(self.english.get())

            total = int((math + chinese + english) / 3)

            dict1 = {"name": name, "chinese": chinese, "math": math, "english": english, "total": total}

            self.label.config(text='修改成功')
            return self.change(dict1)

        except Exception:
            self.label.config(text=f"{self.name.get()}不存在")



root = tk.Tk()
root.geometry('500x300+150+150')
change_frame = ChangeFrame(root)
change_frame.pack()

root.mainloop()
