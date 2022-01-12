/*
teacher
id	            员工id
name	        员工名字
age	            年龄
salary	        薪水
phone	        电话号码
in_department	所处部门

('刘岩', 50, 2485, '13780795566', '数学'),
('张华', 34, 3707, '13799441431', '数学'),
('王健', 22, 2938, '15055876745', '语文'),
('田丹丹', 51, 3888, '18844659764', '语文'),
('颜秀云', 42, 2148, '18761783434', '数学'),
('胡彬', 38, 3219, '18915977888', '数学'),
('王涛', 24, 2064, '13788639370', '数学'),
('宋琴', 48, 2245, '15208504138', '语文'),
('王杨', 25, 2594, '14568517722', '数学'),
('钟畅', 35, 2710, '14717085283', '语文'),

*/
use dzdp;
create table teacher
(
    -- primary key 主键约束 重复就会报错
    -- auto_increment 自动增长 如果不给,就会自动 +1
    id            int primary key auto_increment,
    name          varchar(20),
    age           int,
    salary        float,
    phone         char(11),
    in_department varchar(20)
);
insert into teacher(id, name, age, salary, phone, in_department)
values (1, '刘岩', 50, 2485, '13780795566', '数学');

insert into teacher(id, name, age, salary, phone, in_department)
values (2, '张华', 34, 3707, '13799441431', '数学');

insert into teacher(name, age, salary, phone, in_department)
values ('王健', 22, 2938, '15055876745', '语文');

-- salary 不插入,就设置为 2500 默认值约束
drop table teacher;
create table teacher
(
    id            int primary key auto_increment,
    name          varchar(20),
    age           int,
    salary        float       default 2500, -- 默认值约束,如果不填就给默认的值
    phone         char(11),
    in_department varchar(20) default '培训中心'
);

insert into teacher(name, age, phone, in_department)
values ('田丹丹', 51, '18844659764', '语文');
insert into teacher(name, age, phone)
values ('颜秀云', 42, '18761783434');

select *
from teacher;

-- 非空约束 禁止为空
drop table teacher;
create table teacher
(
    id            int primary key auto_increment,
    name          varchar(20) not null,
    age           int,
    salary        float       null default 2500, -- 默认值约束,如果不填就给默认的值
    phone         char(11)    not null unique,   -- unique 唯一约束
    in_department varchar(20) null default '培训中心'
);

insert into teacher(name, age, phone, in_department)
values ('田丹丹', 51, '18844659764', '语文');

insert into teacher(name, age, salary, phone, in_department)
values ('刘岩', 50, 2485, '', '数学');

insert into teacher(name, age, salary, phone, in_department)
values ('王健', 22, 2938, '', '语文');

insert into teacher(name, age, salary, phone, in_department)
values ('王涛', 24, 2064, '18844659764', '数学');
