# 导入 pymysql 链接数据库
import pymysql

# 1. 创建链接对象
connection = pymysql.connect(
    host='159.75.114.202',  # 数据库服务器的地址
    user='windows',  # 用户名
    password='123456',  # 用户密码
    database='python',  # 操作的数据库
    port=3306
)
print('链接对象:\t', connection)

# 2. 获取游标对象 (执行sql 指令)
cursor = connection.cursor()

# 3. 执行 sql 执行
sql = 'show databases;'
count = cursor.execute(sql)
print('执行sql之后,受影响的行数:\t', count)

# 4. 获取查询结果
results = cursor.fetchall()
print('查询结果:\t', results)
for result in results:
    print(result[0])

# 5. 关闭与服务器的链接
cursor.close()
connection.close()


"""
    socket 

"""
