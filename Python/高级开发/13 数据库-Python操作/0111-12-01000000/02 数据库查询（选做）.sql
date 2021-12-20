-- 查询 电影名,评分,关注数
select movie_name, score, follows
from `16_00_zx`.douban;

-- 求所有电影的平均分数 保留两位小数
select round(avg(score), 2) as avg_score
from `16_00_zx`.douban;
-- 查询每部电影中评分 最高、最低、平均评分、数量
select max(score)           as max_score,
       min(score)           as min_score,
       round(avg(score), 1) as avg_score,
       count(*)             as total
from `16_00_zx`.douban;
-- 查询所有关注数大于平均关注数的电影，并且按评分降序排序

select avg(follows)
from `16_00_zx`.douban;

select *
from `16_00_zx`.douban
where follows > 1165462.6078;

-- 子查询
select *
from `16_00_zx`.douban
where follows > (select avg(follows) from `16_00_zx`.douban);


-- 查询每部电影中评分 最高、最低、平均评分、数量 --> 最终之后一条结果
select max(score)           as max_score,
       min(score)           as min_score,
       round(avg(score), 1) as avg_score,
       count(*)             as total

#        movie_name
from `16_00_zx`.douban;

select movie_name
from `16_00_zx`.douban; # 会有很多条结果