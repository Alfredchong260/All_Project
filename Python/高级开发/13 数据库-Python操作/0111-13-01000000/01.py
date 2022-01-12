# 将changsha.csv的数据保存到数据库，数据表自己设计
"""
 将 changsha.csv 处理成可以给sql直接插入的数据，然后保存到 changsha_result.csv 文件
"""
import pymysql

connection = pymysql.connect(
    host='159.75.114.202',
    user='windows',
    password='123456',
    database='12_10067816_钟满祥',
    port=3306
)

cursor = connection.cursor()

fieldnames = [
              'city',  # 城市
              'region',  # 行政区
              'title',  # 门店名称
              'star_level',  # 星级
              'star',  # 星级得分
              'review_num',  # 点评总数
              'mean_price',  # 人均消费
              "comment_list1",  # 口味
              "comment_list2",  # 环境
              "comment_list3",  # 环境
              "link",  # 链接网址
              "shop_tag_cate_click",  # 分类
              "shop_tag_region_click",  # 商圈
              "addr",  # 详细地址
              ]

create = '''create table changsha(
        id int primary key auto_increment,
        city varchar(3),
        region varchar(5),
        title varchar(20),
        star_level varchar(10),
        star float,
        review_num int,
        mean_price varchar(10),
        comment_list1 float,
        comment_list2 float,
        comment_list3 float,
        link varchar(100),
        shop_tag_cate_click varchar(20),
        shop_tag_region_click varchar(20),
        addr varchar(50)
);'''

# cursor.execute(create)
# connection.commit()

with open('./changsha.csv', 'r', encoding='gbk') as fs:
    lines = fs.readlines()

insert = 'insert to changsha(city, region, title, star_level, star, review_num, mean_price, comment_list1, comment_list2, comment_list3, link, shop_tag_cate_click, shop_tag_region_click, addr) value (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s, %s, %s);'
for line, fieldname in zip(lines, fieldnames):
    try:
        data = tuple(line.strip().split(','))
        cursor.execute(insert, data)
        # canshu = '%s ' * len(data)
        # cursor.execute(insert, tuple(data))
        # break

    except Exception as e:
        print('出错', e)
        connection.rollback()
