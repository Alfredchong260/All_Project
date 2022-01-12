"""
    1. 使用约束创建 employee.txt salary.txt 文件的数据表,并且用外键关联起来
    2. 使用联结查询, 查询员工的个人信息与公司的信息.
"""
import pymysql

connection = pymysql.connect(host='159.75.114.202', user='windows', password='123456', database='company', port=3306)
cursor = connection.cursor()  # 做事的人

# employee_sql = 'insert into employee(name, gender, birth, phone, email, address, id_card) values (%s, %s, %s, %s, %s, %s, %s);'
# lines = open('employee.txt', mode='r', encoding='utf-8').readlines()
# for line in lines:
#     line = tuple(line.strip().split(','))
#     cursor.execute(employee_sql, line)

# 获取到的数据与数据库的格式不一致
salary_sql = 'insert into salary(dept, position, salary, employee_id) values (%s, %s, %s, %s);'
search_sql = 'select id from employee where name=%s;'
lines = open('salary.txt', mode='r', encoding='utf-8').readlines()
for line in lines:
    line = tuple(line.strip().split(','))
    # cursor.execute(salary_sql, line)
    cursor.execute(search_sql, (line[0],))
    employee_id = cursor.fetchone()
    print(employee_id)
    print(line)
    cursor.execute(salary_sql, (line[1], line[2], line[3], employee_id[0]))

connection.commit()
cursor.close()
connection.close()
