"""
    1. 使用约束创建 employee.txt salary.txt 文件的数据表,并且用外键关联起来
    2. 使用联结查询, 查询员工的个人信息与公司的信息.
"""

import pymysql

connection = pymysql.connect(
    host='159.75.114.202', user='windows', password='123456', database='12_10067816_钟满祥')

cursor = connection.cursor()

drop = 'drop table employee;'
drop1 = 'drop table salary;'
cursor.execute(drop)
cursor.execute(drop1)
connection.commit()

create_employee_table = '''create table employee(
    id int primary key auto_increment,
    name varchar(255) not null,
    gender varchar(2) not null default '女',
    birth datetime not null,
    phone varchar(11) not null,
    email varchar(255) not null,
    address varchar(255) not null,
    ic_num varchar(18) not null unique
);'''

create_salary_table = '''create table salary(
    id int primary key auto_increment,
    name varchar(255) not null,
    department varchar(10) not null,
    office varchar(10) not null,
    salary int default '2500'
);'''

cursor.execute(create_employee_table)
cursor.execute(create_salary_table)
connection.commit()

create = 'insert into employee(name, gender, birth, phone, email, address, ic_num) values (%s, %s, %s, %s, %s, %s, %s)'

with open('./employee.txt', 'r', encoding='utf-8') as r:
    infos = r.read().strip().split('\n')
    for info in infos:
        data = tuple(info.split(','))
        try:
            cursor.execute(create, data)
            connection.commit()
        except Exception as e:
            print('出错', e)
            connection.rollback()

create2 = 'insert into salary(name, department, office, salary) values (%s, %s, %s, %s)'

with open('./salary.txt', 'r', encoding='utf-8') as fs:
    lines = fs.readlines()
    for line in lines:
        data = tuple(line.strip().split(','))
        try:
            cursor.execute(create2, data)
            connection.commit()
        except Exception as e:
            print('出错', e)
            connection.rollback()

combine_search = ''' select e.name, e.gender, e.birth, e.phone, e.address, e.ic_num, s.department, s.office, s.salary
    from employee as e
        inner join salary s on s.name = e.name;
'''

cursor.execute(combine_search)
info = cursor.fetchall()
print(info)
