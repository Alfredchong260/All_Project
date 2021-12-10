""""""
import json

"""
    参考 `学生信息管理系统-数据修改.png` 实现学生信息管理系统的修改部分布局与逻辑代码
    
    首先输入名字，查询学生信息
        如果没有查询到信息，就显示此学生不存在
        查询到了信息，就将信息显示到页面上
    可以随意修改页面是显示的学生信息，修改完之后点击提交就能完成修改
"""
import tkinter as tk


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


class ChangeFrame(tk.Frame):  # 继承Frame类
    def __init__(self, master=None):
        super().__init__(master)
        self.status = tk.StringVar()
        self.name = tk.StringVar()
        self.math = tk.StringVar()
        self.chinese = tk.StringVar()
        self.english = tk.StringVar()

        self.create_page()

    def create_page(self):
        # 补全创建页面逻辑
        tk.Label(self).grid(row=0, sticky=tk.W, pady=1)
        tk.Label(self, text='姓 名: ').grid(row=1, stick=tk.W, pady=10)
        tk.Entry(self, textvariable=self.name).grid(row=1, column=1, stick=tk.E)
        tk.Label(self, text='数 学: ').grid(row=2, stick=tk.W, pady=10)
        tk.Entry(self, textvariable=self.math).grid(row=2, column=1, stick=tk.E)
        tk.Label(self, text='语 文: ').grid(row=3, stick=tk.W, pady=10)
        tk.Entry(self, textvariable=self.chinese).grid(row=3, column=1, stick=tk.E)
        tk.Label(self, text='英 语: ').grid(row=4, stick=tk.W, pady=10)
        tk.Entry(self, textvariable=self.english).grid(row=4, column=1, stick=tk.E)
        tk.Button(self, text='查询', command=self._search).grid(row=6, column=0, stick=tk.W, pady=10)
        tk.Button(self, text='修改', command=self._change).grid(row=6, column=1, stick=tk.E, pady=10)
        tk.Label(self, textvariable=self.status).grid(row=7, column=1, stick=tk.E, pady=10)

    def _search(self):
        # 1. 获取页面上的名字
        name = self.name.get()
        student = db.search(name)
        if student:
            self.math.set(student['math'])
            self.chinese.set(student['chinese'])
            self.english.set(student['english'])
            self.status.set(f'查询到 {name} 同学的信息')
        else:
            self.status.set(f'没有 {name} 同学的信息')
        # 补全查找逻辑
        pass

    def _change(self):
        # 补全修改数据逻辑
        name = self.name.get()
        math = self.math.get()
        chinese = self.chinese.get()
        english = self.english.get()
        stu = {
            'name': name,
            'math': math,
            'chinese': chinese,
            'english': english,
        }
        r = db.change(stu)
        if r:
            self.status.set(f'{name} 同学的信息更新完毕')
        else:
            self.status.set(f'{name} 同学的信息更新失败')


root = tk.Tk()
root.geometry('500x300+150+150')
# 创建一个布局组件,然后布局,所有的逻辑就都实现了
change_frame = ChangeFrame(root)
change_frame.pack()

root.mainloop()
