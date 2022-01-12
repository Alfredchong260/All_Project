use dzdp;
truncate changsha;
-- 一页10条数据
/*
page: 第几页
pre_page: 一个多少条数据
查询第几页的公式: limit (page-1)*pre_page, pre_page
*/
select *
from changsha
limit 0, 10;

select *
from changsha
limit 10, 10;
-- 一页50条,查询第五页
select *
from changsha
limit 200, 50;

show tables ;
