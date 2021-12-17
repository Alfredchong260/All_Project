show databases;
use python;
/*
    请为下面这些数据新建一个数据表，并将其写入。

    ('主演：秦岚,糸井重里,岛本须美', '龙猫', '上映时间：2018-12-14', '9.1'),
    ('主演：张国荣,张曼玉,刘德华', '阿飞正传', '上映时间：2018-06-25', '8.8'),
    ('主演：俞承豪,金艺芬,童孝熙', '爱·回家', '上映时间：2002-04-05(韩国)', '9.0'),
    ('主演：雅克·贝汉,姜文,兰斯洛特·佩林', '海洋', '上映时间：2011-08-12', '9.0'),
    ('主演：宋在浩,李顺才,尹秀晶', '我爱你', '上映时间：2011-02-17(韩国)', '9.0'),
    ('主演：克林特·伊斯特伍德,李·范·克里夫,埃里·瓦拉赫', '黄金三镖客', '上映时间：1966-12-23(意大利)', '8.9'),
    ('主演：雅克·贝汉,Philippe Labro', '迁徙的鸟', '上映时间：2001-12-12(法国)', '9.1'),
    ('主演：柊瑠美,周冬雨,入野自由', '千与千寻', '上映时间：2019-06-21', '9.3'),
    ('主演：蒂姆·罗斯,比尔·努恩,普路特·泰勒·文斯', '海上钢琴师', '上映时间：2019-11-15', '9.3'),
    ('主演：菲利浦·诺瓦雷,赛尔乔·卡斯特利托,蒂兹亚娜·罗达托', '天堂电影院', '上映时间：2019-06-15', '9.2')
*/
drop table top100;
create table top100
(
    id      int primary key auto_increment,
    star    varchar(29),
    name    varchar(20),
    publish varchar(20),
    score   float
);

-- 删除数据表,重新插入数据
select *
from top100;

desc top100;
-- 修改字段
alter table top100
    modify column name varchar(200);

-- 新增字段
alter table top100
    add column country varchar(20);

-- 删除字段
alter table top100
    drop column country;

-- 重命名字段
alter table top100 change country country2 varchar(20);

-- UPDATE 表名 SET 字段名=值,字段名=值
-- WHERE 筛选条件;
update top100
set country='日本'
where name = '龙猫';
