show databases;
use python;

# char 固定长度的字符串
# varchar 变长字符串(最长 255 的长度)
# datetime
# Text

-- sql 不区分大小写
create table student
(
    id      int primary key auto_increment, -- 主键,数据约束的时候详细键
    name    varchar(50),                    -- 人名应该给多少位
    math    float,
    chinese float,
    english float,
    phone   char(11)                     -- 电话号码应该是什么类型,以及给多长?
);

desc student;

