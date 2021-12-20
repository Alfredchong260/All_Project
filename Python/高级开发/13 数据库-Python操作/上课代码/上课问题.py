# 'update students2 set math=%s,chinese=%s,english=%s where name=%s;'

sql_format = 'update students2 set {} where name=%s;'

# math=%s,chinese=%s,english=%s
# math
# math chinese

args = ['math', 'chinese']
args_str = '=%s,'.join(args) + '=%s'
print(sql_format.format(args_str))


import pymysql

connection = pymysql.connect(host='159.75.114.202', user='windows', password='123456', database='python', port=3306)
cursor = connection.cursor()  # 做事的人
# 并发情况下,可以使用多个游标对象

# 1. 准备需要执行的sql
sql = 'desc students2;'
count = cursor.execute(sql)
fields = cursor.fetchall()
new_fields = [field[0] for field in fields]
new_fields.remove('math')
new_fields.remove('id')
print(new_fields)
cursor.close()
connection.close()
