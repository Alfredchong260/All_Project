""""""
"""
    将学生信息管理系统页面上的录入学生信息逻辑，单独封装成一个类
    
    当点击录入学生信息时，将数据保存到数据操作的类中。
"""
"""自己在下方编写代码实现功能"""
import tkinter as tk
import csv


class DataBase:
    def __init__(self):
        self.students = []
        self.fs = open('data.csv', 'a', encoding='utf-8', newline='')
        self.csv_writer = csv.writer(self.fs)

    def append(self, stu):
        self.students.append(stu)

    def insertData(self):
        for data in self.students:
            self.csv_writer.writerow(data)

db = DataBase()

class InputFrame:  # 继承Frame类
    def __init__(self):
        self.root = tk.Tk()
        menu_bar = tk.Menu(self.root)
        add_menu = tk.Menu(menu_bar)
        menu_bar.add_cascade(label="文件", menu=add_menu)

        search_menu = tk.Menu(menu_bar)
        menu_bar.add_cascade(label="编辑", menu=search_menu)

        del_menu = tk.Menu(menu_bar)
        menu_bar.add_cascade(label="删除", menu=del_menu)

        change_menu = tk.Menu(menu_bar)
        menu_bar.add_cascade(label="修改", menu=change_menu)

        about_menu = tk.Menu(menu_bar)
        menu_bar.add_cascade(label="关于", menu=about_menu)

        self.root.config(menu=menu_bar)
        self.root.geometry('500x300')

        self.frame = tk.Frame(self.root)
        self.frame.pack()
        self.name = tk.StringVar()
        self.math = tk.StringVar()
        self.chinese = tk.StringVar()
        self.english = tk.StringVar()
        self.status = tk.StringVar()
        self.create_page()

        self.root.mainloop()

    def create_page(self):
        # stick 控件对象方向 tk.W 西方位
        # pady padding y 上下的宽度
        # row 行 表格布局
        tk.Label(self.frame).grid(row=0, column=0, stick=tk.W, pady=10)
        tk.Label(self.frame, text='姓 名: ').grid(row=1, column=0, stick=tk.W, pady=10)
        # text variable 绑定控件里面的数据内容
        tk.Entry(self.frame, textvariable=self.name).grid(row=1, column=1, sticky=tk.E)
        tk.Label(self.frame, text='数 学: ').grid(row=2, column=0, sticky=tk.W, pady=10)
        tk.Entry(self.frame, textvariable=self.math).grid(row=2, column=1, sticky=tk.E)
        tk.Label(self.frame, text='语 文: ').grid(row=3, column=0, sticky=tk.W, pady=10)
        tk.Entry(self.frame, textvariable=self.chinese).grid(row=3, column=1, sticky=tk.E, pady=10)
        tk.Label(self.frame, text='英 语: ').grid(row=4, column=0, sticky=tk.W, pady=10)
        tk.Entry(self.frame, textvariable=self.english).grid(row=4, column=1, sticky=tk.E, pady=10)
        tk.Button(self.frame, text='录入', command=self.recode_student).grid(row=5, column=1, sticky=tk.E, pady=10)
        tk.Label(self.frame, textvariable=self.status).grid(row=6, column=1, sticky=tk.E, pady=10)

    def recode_student(self):
        student = {
            'name': self.name.get(),
            'math': self.math.get(),
            'chinese': self.chinese.get(),
            'english': self.english.get(),
        }
        db.append(student)
        self.status.set('插入数据成功')
        self._clear_avr()

    def _clear_avr(self):
        self.name.set("")
        self.math.set("")
        self.chinese.set("")
        self.english.set("")


if __name__ == '__main__':
    InputFrame()
