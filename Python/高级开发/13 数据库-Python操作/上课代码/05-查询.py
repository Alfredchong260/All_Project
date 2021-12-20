import pymysql

connection = pymysql.connect(host='159.75.114.202', user='windows', password='123456', database='python', port=3306)
cursor = connection.cursor()  # 做事的人
# 并发情况下,可以使用多个游标对象
cursor2 = connection.cursor()  # 做事的人

# 1. 准备需要执行的sql
sql = 'select * from student;'

# 2. 执行 sql  --> 返回的结果是一个生成器
count = cursor.execute(sql)

# 3. 获取查询的数据
print('收影响的行数:\t', count)
print('获取一条数据:\t', cursor.fetchone())
print('获取多条数据:\t', cursor.fetchmany(5))

# 之前的数据还没有查询完,又执行了新的查询, 新查询结果就会将旧的覆盖掉
sql2 = 'select id, no, name, birth from student;'
cursor2.execute(sql2)
print('cursor 获取所有的数据:\t', cursor.fetchall())
print('cursor2 获取所有的数据:\t', cursor2.fetchall())

cursor.close()
connection.close()
