import pymysql

connection = pymysql.connect(
    host='159.75.114.202',  # 数据库服务器的地址
    user='windows',  # 用户名
    password='123456',  # 用户密码
    database='16_00_zx',  # 操作的数据库
    port=3306
)
print('链接对象:\t', connection)

cursor = connection.cursor()

# 需要执行的原生 sql
# 能不能字符串拼接构建需要执行的 sql ?
sql = 'insert into douban(movie_name, other_name, info, score, follows) values ("肖申克的救赎","肖申克的救赎/ The Shawshank Redemption/ 月黑高飞(港)  /  刺激1995(台)","导演: 弗兰克·德拉邦特 Frank Darabont   主演: 蒂姆·罗宾斯 Tim Robbins /...1994 / 美国 / 犯罪 剧情","9.7","1981964");'

count = cursor.execute(sql)
print('执行sql之后,受影响的行数:\t', count)

connection.commit()  # 保存修改

cursor.close()
connection.close()
