use dzdp;

create table teacher
(
    id     int primary key auto_increment,
    name   char(3),
    office char(4)
);

create table students
(
    id      int primary key auto_increment,
    name    char(3),
    subject char(4)
);

create table association
(
    id         int primary key auto_increment,
    student_id int,
    teacher_id int,
    constraint fk_student foreign key (student_id) references students (id),
    constraint fk_teacher foreign key (teacher_id) references teacher (id)
);

-- 联结查询
-- 先分数,再名字
select s.id as id, s.name as name, s.subject as subject, office, t.name as teacher_name
from association as a -- 用关系表作为主表
         inner join students s on a.student_id = s.id
         inner join teacher t on a.teacher_id = t.id
;

/*
    一开始表没有拆分

    之后进行了拆分

    view_info
*/
-- 创建一个视图(虚拟表)
CREATE VIEW view_info (id, name, subject, office, teacher_name) AS
    -- 虚拟表的查询逻辑
select s.id as id, s.name as name, s.subject as subject, office, t.name as teacher_name
from association as a -- 用关系表作为主表
         inner join students s on a.student_id = s.id
         inner join teacher t on a.teacher_id = t.id
;
show tables ;

-- 把视图当做普通表进行使用, 在查询的时候还是会执行联结查询的逻辑
select name, subject from view_info;
