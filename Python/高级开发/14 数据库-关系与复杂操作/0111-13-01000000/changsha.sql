create database dzdp character set 'utf8mb4';
use dzdp;
create table changsha
(
    id                    int primary key auto_increment,
    city                  varchar(255),
    region                varchar(255),
    title                 varchar(255),
    star_level            varchar(255),
    star                  varchar(255),
    review_num            varchar(255),
    mean_price            varchar(255),
    comment_list1         varchar(255),
    comment_list2         varchar(255),
    comment_list3         varchar(255),
    link                  varchar(255),
    shop_tag_cate_click   varchar(255),
    shop_tag_region_click varchar(255),
    addr                  varchar(255)
);

desc changsha;
-- '姓名: %s 年龄:%s' % ('正心', 18)
insert into changsha(city, region, title, star_level, star, review_num, mean_price, comment_list1, comment_list2,
                     comment_list3, link, shop_tag_cate_click, shop_tag_region_click, addr)
values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);

select *
from changsha;

-- 通过名字查询, 默认按照顺序,需要找391次才能找到
select *
from changsha
where title = '烤肴烧烤(太平街店)';

show index from changsha;
ALTER TABLE changsha ADD INDEX idx_title (title);

# insert into changsha()
/*
    索引会进行排序,以及有其他优化
    索引一般会有查询优化  其中有一个算法叫 二分法
    索引查询速度快 --> 修改数据速度变慢

    读写分离  一个写很多个读

391  拿快递

         250
                375

                        406
                    437
    500
1000
*/