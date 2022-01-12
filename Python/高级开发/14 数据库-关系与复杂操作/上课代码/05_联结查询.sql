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
select s.id, s.name, s.subject, office, t.name
from association as a -- 用关系表作为主表
         inner join students s on a.student_id = s.id
         inner join teacher t on a.teacher_id = t.id
;


