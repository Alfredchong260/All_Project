# -*- coding: utf-8 -*-
import pymysql


class Databases:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',
                                    port=3306,
                                    database='python',
                                    user='root',
                                    password='root',
                                    charset='utf8')
        self.cursor = self.conn.cursor()

    def fetch_students(self):
        sql = 'select * from student_info;'
        self.cursor.execute(sql)
        students = self.cursor.fetchall()
        rets = []
        for student in students:
            rets.append({
                'id': student[0],
                'no': student[1],
                'name': student[2],
                'email': student[3],
                'gender': student[4],
                'city': student[5],
            })
        return rets


db = Databases()
if __name__ == '__main__':
    print(db.fetch_students())
