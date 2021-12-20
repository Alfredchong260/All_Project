# sql 注入

import pymysql

connection = pymysql.connect(host='159.75.114.202', user='windows', password='123456', database='python', port=3306)
cursor = connection.cursor()  # 做事的人

# 根据名字查询学生
# sql = "select * from student where name='%s';"
# name = input('请输入你想要查询的学生姓名:')
# target_sql = sql % (name,)
# print('target_sql:\t', target_sql)
# cursor.execute(target_sql)
# 参数化,字符串格式化不加单引号

sql = "select * from student where name=%s;"
name = input('请输入你想要查询的学生姓名:')
# 参数化防止注入
cursor.execute(sql, (name,))
for result in cursor.fetchall():
    print(result)

# 'or 1=1 or ' sql 注入

"""
    sql 注入在搜索内容的时候可能出出现
    如果用字符串拼接就可能出现注入的问题
    '正心' --> select * from student where name='正心';
    'or 1=1 or ' --> select * from student where name=''or 1=1 or '';
    'or 1=1 or ' --> select * from student where name='%%';
    
    注入是查询一段逻辑
"""

cursor.close()
connection.close()
