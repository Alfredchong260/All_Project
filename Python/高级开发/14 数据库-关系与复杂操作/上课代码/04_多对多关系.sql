use dzdp;
# drop table teacher;
# drop table students;
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

/*
    ORM 关系模型对象
*/

insert into teacher(id, name, office)
values (1, '张三', '语文老师'),
       (2, '李四', '历史老师'),
       (3, '王五', '物理老师')
;

insert into students(id, name, subject)
values (1, '小红', '文科'),
       (2, '小绿', '文科'),
       (3, '小灰', '理科'),
       (4, '小黑', '理科')
;

insert into association(student_id, teacher_id)
values (1, 1),
       (2, 1),
       (3, 1),
       (4, 1),
       (1, 2),
       (2, 2),
       (3, 3),
       (4, 3)
;

select *
from students;
select *
from teacher;
select *
from association;

-- 获取 张三 老师带的所有的学生
select id
from teacher
where name = '张三';
-- 先通过关系找到所有的学生 id
select student_id
from association
where teacher_id = 1;
--
select *
from students
where id in (1, 2, 3, 4);


select *
from students
where id in (select student_id
             from association
             where teacher_id = (select id
                                 from teacher
                                 where name = '李四'));
