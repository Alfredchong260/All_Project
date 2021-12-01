""""""
import json

"""
    将基础课的学生信息管理系统中的数据操作抽象为一个类

    类名：MySqlDB
    属性：students
    方法：insert、delete、change、search、save
    
    
    1. 启动程序，加载 students.json 文件里面的数据
    2. 实现增删改查
    3. 退出系统之前保存数据
"""


# 只要操作数据就行了
class MySqlDB:

    def __init__(self, filename):
        self.students = []
        self.filename = filename
        self.load()

    def load(self):
        with open(self.filename, mode='r', encoding='utf-8') as f:
            text = f.read()
        self.students.extend(eval(text))

    def all(self):
        return self.students

    def search(self, name):
        for student in self.students:
            if student['name'] == name:
                return student
        return False

    def change(self, stu):
        student = self.search(stu['name'])

        if student:
            # student['name'] = stu['name']
            # student['chinese'] = stu['chinese']
            # student['math'] = stu['math']
            # student['english'] = stu['english']
            # student['total'] = stu['total']
            student.update(stu)  # 字典的更新方法
        else:
            return False


db = MySqlDB('students.json')
print(db.all())
print(db.search('李四'))
print(db.change({'name': '李四', 'chinese': 100, 'math': 100, 'english': 100, 'total': 100}))
# print(db.all())
print(db.search('李四'))
