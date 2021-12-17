use 12_10067816_钟满祥;

-- 查询 电影名,评分,关注数
select movie_name, score, follows from douban;

-- 求所有电影的平均分数 保留两位小数
select round(avg(score), 2) from douban;

-- 查询每部电影中评分 最高、最低、平均评分、数量
select
round(max(score), 2) as max,
round(min(score), 2) as min,
round(avg(score), 2) as average,
count(score) as total
from douban;

-- 查询所有关注数大于平均关注数的电影，并且按评分降序排序
select * from douban
where follows > (select avg(follows) from douban)
order by score desc;
