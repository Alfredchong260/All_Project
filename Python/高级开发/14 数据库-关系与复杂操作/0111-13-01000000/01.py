# 将changsha.csv的数据保存到数据库，数据表自己设计
"""
 将 changsha.csv 处理成可以给sql直接插入的数据，然后保存到 changsha_result.csv 文件
"""
import pymysql

fieldnames = ['city',  # 城市
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
conn = pymysql.connect(
    user='windows',  # The first four arguments is based on DB-API 2.0 recommendation.
    password="123456",
    host='159.75.114.202',
    database='dzdp',
)

cursor = conn.cursor()
sql_format = 'insert into changsha(city, region, title, star_level, star, review_num, mean_price, comment_list1, comment_list2, comment_list3, link, shop_tag_cate_click, shop_tag_region_click, addr) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'

with open('changsha.csv', mode='r', encoding='gbk') as f:
    lines = f.readlines()
    for line in lines:
        try:
            data = tuple(line.strip().split(','))
            # print(data)
            cursor.execute(sql_format, data)
            conn.commit()
        except Exception as e:
            print(e, data)  # 出错将错误信息收集起来

cursor.close()
conn.close()
