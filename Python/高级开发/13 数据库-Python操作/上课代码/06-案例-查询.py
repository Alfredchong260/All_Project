"""
    用面向对象的方式操作数据库
    实现对学员数据的增删改查

    insert
    search_by_name
    delete_by_name
    update_by_name
"""
import pymysql


class Student:
    """面向对象封装查询"""

    def __init__(self):
        self.connection = pymysql.connect(host='159.75.114.202',
                                          user='windows',
                                          password='123456',
                                          database='python',
                                          port=3306)
        self.cursor = self.connection.cursor()  # 做事的人

    def insert(self, student):
        """插入的方法"""
        insert_sql_template = "insert into student(no, name, gender, birth, phone, email, address, id_card)values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');"
        self.cursor.execute(insert_sql_template % student)
        self.connection.commit()

    def search_by_name(self, name):
        sql = "select * from student where name='%s';"
        self.cursor.execute(sql % (name,))
        # sql % (name,) -- > "select * from student where name='%s';" % (name,)
        # sql % (name,) -- > "select * from student where name='%s' and gedner='%s';" % (name, gender)
        return self.cursor.fetchall()

    def search_by_gender(self, gender='男'):
        sql = "select * from student where gender='%s';"
        self.cursor.execute(sql % (gender,))
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()


if __name__ == '__main__':
    db = Student()
    student = (
        '319044', '正心', '男', '1998/3/26', '14208332532', '518110817@qq.com', '上海市杨浦区邯郸路224号', '340825199902250210')
    # db.insert(student)
    print(db.search_by_name('正心'))
    print(db.search_by_gender())
