import pymysql

connection = pymysql.connect(host='159.75.114.202', user='windows', password='123456', database='python', port=3306)
cursor = connection.cursor()

with open('student.txt', mode='r', encoding='utf-8') as f:
    lines = f.readlines()

for line in lines:  # 第七条数据会报错
    try:
        student = tuple(line.strip().split(','))
        insert_sql_template = "insert into student(no, name, gender, birth, phone, email, address, id_card)values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');"
        print(insert_sql_template % student)
        cursor.execute(insert_sql_template % student)
        connection.commit()  # 插入成功之后立马进行提交,每一条数据都会提交一次
    except Exception as e:
        # 如果出错了,就全部不提交
        # 事务,一起成功一起失败
        connection.rollback()  # 回滚,撤销没有保存到本地的提交
        print("出错啦")

# 忽略出错的那一条数据,其余的正常运行

# 提交,保存更改
connection.commit()   # 最后提交,保存一次
cursor.close()
connection.close()

"""
    phpstudy 每一次提交都会主动保存到本地
    
    充Q币
    
    钱从支付宝转出去了
    心悦会员app 还没有到账
    
    mysql 数据库最大的优点  postgresql 
    
    关系型
"""
