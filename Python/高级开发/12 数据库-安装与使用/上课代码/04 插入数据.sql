show databases;
use python;

drop table student;
-- sql 不区分大小写
create table student
(
    id      int primary key auto_increment, -- 主键,数据约束的时候详细键
    name    varchar(50),                    -- 人名应该给多少位
    math    float,
    chinese float,
    english float
);

/*
INSERT INTO 表名(字段列表)
VALUES(字段值列表),(字段值列表),(字段值列表),(字段值列表);
*/
-- 一般不手动插入 id 字段
insert into student(name, math, chinese, english) value ('张三', '60', '60', '60');
insert into student(name, math, chinese, english) value ('李四', '60', '60', '60');
insert into student(name, math, chinese, english) value ('王五', '60', '60', '60');

insert into student(name, math, chinese, english)
values ('张三', '60', '60', '60'),
       ('李四', '60', '60', '60'),
       ('王五', '60', '60', '60');

select *
from student;

# 更新数据
/*UPDATE 表名 SET 字段名=值,字段名=值 WHERE 筛选条件;*/
UPDATE student SET chinese=100 WHERE name='张三';
UPDATE student SET english=100 WHERE id=1;


/*DELETE FROM 表名 WHERE 筛选条件;*/
delete from student where id=1;
