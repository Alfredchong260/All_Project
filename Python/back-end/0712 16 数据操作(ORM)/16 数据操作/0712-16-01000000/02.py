""""""
"""
利用利用下的信息创建两种数据表，并且建立双向关系。
可以根据学生找到老师，也可以通过老师找到所有的学生
"""
"""
班主任（teachers）：
CREATE TABLE teachers
(
    id            INT PRIMARY KEY AUTO_INCREMENT,
    name          varchar(20),
    age           int,
    salary        float,
    phone         char(11),
) character set utf8;
-- 插入三条数据
/*
('刘岩', 50, 2485, '13780795566'),
('张华', 34, 3707, '13799441431'),
('王健', 22, 2938, '15055876745')
*/

学员表(students)：
create table student
(
    id           int primary key auto_increment,
    name         varchar(20) not null,
    chinese      int,
    rank         int,
    teacher_id   int
);
('刘岩', 50, 2485, '1'),
('张华', 34, 3707, '1'),
('王健', 22, 2938, '1'),
('田丹丹', 51, 3888, '2'),
('颜秀云', 42, 2148, '2'),
('胡彬', 38, 3219, '2'),
('王涛', 24, 2064, '3'),
('宋琴', 48, 2245, '3'),
('王杨', 25, 2594, '3'),
('钟畅', 35, 2710, '3'),
"""