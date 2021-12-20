import json

import pymysql


class StudentsDB:
    """学生信息管理系统数据模型"""

    def __init__(self):
        self.students = []
        # 加载本地文件中的数据
        self._load_students_data()

    def insert(self, student):
        """将学生数据插入到列表"""
        self.students.append(student)

    def all(self):
        """返回所有的学生数据"""
        return self.students

    def delete_by_name(self, name):
        """根据名字获取学生数据，如果没有就返回 False"""
        for student in self.students:
            if name == student['name']:
                self.students.remove(student)
                break
        else:
            return False
        return True

    def search_by_name(self, name):
        """根据名字查询学员，没有找到就返回 False"""
        for student in self.students:
            if name == student['name']:
                return student
        else:
            return False

    def update(self, stu):
        """更新学员信息"""
        name = stu['name']
        for student in self.students:
            if name == student['name']:
                student.update(stu)
                return True
        else:
            return False

    def _load_students_data(self):
        """从本地文件中加载数据"""
        with open('students.json', mode='r', encoding='utf-8') as f:
            text = f.read()
        if text:
            self.students = json.loads(text)

    def save_data(self):
        """保存数据到本地文件"""
        with open('students.json', mode='w', encoding='utf-8') as f:
            text = json.dumps(self.students, ensure_ascii=False)
            f.write(text)


class StudentsMysqlDb:
    def __init__(self):
        self.connection = pymysql.connect(host='159.75.114.202',
                                          user='windows',
                                          password='123456',
                                          database='python',
                                          port=3306)
        self.cursor = self.connection.cursor()  # 做事的人

    def insert(self, student):
        # {"name": "张三", "math": "65", "chinese": "75", "english": "100"}
        _student = (student['name'], student["math"], student["chinese"], student["english"])
        sql = 'insert into students2(name, math, chinese, english) value (%s,%s,%s,%s);'
        self.cursor.execute(sql, _student)
        self.connection.commit()

    def all(self):
        """返回所有的学生数据"""
        sql = 'select name,math,chinese,english from students2;'
        self.cursor.execute(sql)
        _students = self.cursor.fetchall()
        students = [
            {
                "name": student[0], "math": student[1],
                "chinese": student[2], "english": student[3]
            } for student in _students]
        return students

    def delete_by_name(self, name):
        sql = 'delete from students2 where name=%s;'
        self.cursor.execute(sql, (name,))
        self.connection.commit()

    def search_by_name(self, name):
        """根据名字查询学员，没有找到就返回 False"""

        sql = 'select name,math,chinese,english from students2 where name =%s;'
        self.cursor.execute(sql, (name,))
        _students = self.cursor.fetchall()
        students = [
            {
                "name": student[0], "math": student[1],
                "chinese": student[2], "english": student[3]
            } for student in _students]
        return students[0]

    def update(self, stu):
        sql = 'update students2 set math=%s,chinese=%s,english=%s where name=%s;'
        self.cursor.execute(sql, (stu['math'], stu['chinese'], stu['english'], stu['name']))
        self.connection.commit()

    def save_data(self):
        pass


# db = StudentsDB()

db = StudentsMysqlDb()
# db.insert({"name": "张三", "math": "65", "chinese": "75", "english": "100"})
# print(db.all())
# print(db.search_by_name('张三'))
# print(db.update({"name": "张三", "math": "100", "chinese": "100", "english": "100"}))
# print(db.search_by_name('张三'))
# print(db.delete_by_name('张三'))
# print(db.search_by_name('张三'))
