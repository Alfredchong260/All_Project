"""
    将基础课的学生信息管理系统中的数据操作抽象为一个类

    类名：MySqlDB
    属性：students
    方法：insert、delete、change、search、save
"""


class MySqlDB:
    def __init__(self):
        self.students = [
            {'name': '张三', 'chinese': '59', 'math': '59', 'english': '59'}
        ]

    def insert(self, stu):
        self.students.append(stu)

    def search(self, name):
        """
        查询学员信息,如果找到了就返回学员的信息字典,没有找到就返回None
        :param name: 学员的名字
        :return: dict or None
        """
        for student in self.students:
            if student['name'] == name:
                return student
        return None

    def delete(self, name):
        """
        输入学员的名字,找到之后就删除学员并返回True,没有找到就返回False
        :param name: 学员的名字
        :return: bool
        """
        ret = self.search(name)
        if ret:
            self.students.remove(ret)
        return False

    def all(self):
        return self.students


class SqliteDB:
    def __init__(self):
        pass

    def insert(self, stu):
        pass

    def search(self, name):
        pass

    def delete(self, name):
        pass


db = MySqlDB()
stu = {'name': '李四', 'chinese': '60', 'math': '60', 'english': '60'}
# 新增学员的信息
db.insert(stu)
# 查询学员的信息
print('查找正心:\t', db.search('正心'))
print('查找李四:\t', db.search('李四'))
print('删除正心:\t', db.delete('正心'))
print('删除李四:\t', db.delete('李四'))
"""
    我可以封装一个函数,也可以直接把代码写在逻辑里面,封装的意义在哪里?
    
    
    GUI 版本的学生信息管理系统 --> 页面创建,事件绑定,逻辑操作,数据修改 --> 可以用类进行模块化
    
    当项目发生变化的时候,只要修改部分内容就可以
    
"""
print(db.all())
