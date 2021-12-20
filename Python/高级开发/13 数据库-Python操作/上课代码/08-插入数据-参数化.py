import pymysql

connection = pymysql.connect(host='159.75.114.202', user='windows', password='123456', database='python', port=3306)
cursor = connection.cursor()

# 读取本地文件
with open('student.txt', mode='r', encoding='utf-8') as f:
    lines = f.readlines()

insert_sql_template = "insert into student(no, name, gender, birth, phone, email, address, id_card) value (%s, %s, %s, %s, %s, %s, %s, %s);"
new_students = []
for line in lines:
    student = tuple(line.strip().split(','))
    print(student)
    # 构建 sql 字符串
    # 执行 sql
    new_students.append(student)
    # cursor.execute(insert_sql_template, student)

cursor.executemany(insert_sql_template, new_students)
connection.commit()
cursor.close()
connection.close()
