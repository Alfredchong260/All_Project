/*
    比较运算符 = > < !=
    逻辑运算符 and not or
    身份运算符 in not
    模糊匹配 like _ %
*/
-- 4000 以下的电脑
select *
from goods
where price < 4000;
-- 3000 - 4000 的预算
select *
from goods
where price < 5000
  and price > 3000;


select *
from goods
where price < 5000
  and price > 3000
  and brand_name = '宏碁';

-- 3000 - 5000 的预算，并且想买联想或者苹果的电脑
select *
from goods
where price < 5000
  and price > 3000
  and (brand_name = '宏碁' or brand_name = '苹果');

select *
from goods
where price < 5000
  and price > 3000
  and brand_name in ('宏碁', '苹果');

-- 不看苹果与宏碁的电脑
select *
from goods;
select *
from goods
where brand_name not in ('宏碁', '苹果');
select *
from goods
where brand_name in ('宏碁', '苹果');

-- 模糊匹配
-- 15.6英寸游戏本
select *
from goods
where name LIKE '%15.6%';

-- 排序 升序 asc (默认)， 降序 desc
select *
from goods
where name LIKE '%15.6%'
-- order by 字段 根据某一个字段进行排序，默认是升序
order by price desc;


select *
from goods
order by cate_name, brand_name
;

-- 常用函数
-- 数据库中总共有多少个商品
select count(*) as total
from goods;
select brand_name, count(*) as total
from goods
where brand_name = '联想';
select brand_name, count(*) as total
from goods
where brand_name = '宏碁';

# 分组查询
# 向查看一下每个品牌有多少台电脑
select *
from goods
order by brand_name;

select brand_name
     , count(*) as total
     , avg(price) as avg_price
from goods
group by brand_name;
