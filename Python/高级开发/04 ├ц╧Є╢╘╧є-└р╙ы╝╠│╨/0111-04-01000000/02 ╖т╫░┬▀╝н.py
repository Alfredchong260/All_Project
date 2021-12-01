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

    def __init__(self, students):
        self.students = open(students, 'r', encoding='utf-8')
        self.data = json.load(self.students)

    def insert(self, dict1):
        if dict1 and len(dict1) == 5:
            self.data.append(dict1)
            return '输入成功'
        return '只接受字典形式'

    def all(self):
        return self.data

    def search(self, name):
        for data in self.data:
            if name == data['name']:
                return data

        return None

    def change(self, dict1):
        student = self.search(dict1['name'])
        if student:
            student.update(dict1)
            return '修改成功'
        else:
            return None

    def save(self):
        self.students.close()
        with open('./students.json', 'w', encoding='utf-8') as w:
            w.write(json.dumps(self.data, ensure_ascii=False))
        return 'Success'

    def delete(self, name):
        for data in self.data:
            if name == data['name']:
                self.data.remove(data)
        return None

db = MySqlDB('students.json')
# db.delete('李四')
# print(db.all())
# print(db.insert({'name':'王五', 'chinese':100, 'math':100, 'english':100, 'total': 100}))
print(db.search('李四'))
print(db.change({'name': '李四', 'chinese': 100, 'math': 100, 'english': 100, 'total': 100}))
print(db.all())
# print(db.all())
# print(db.save())
