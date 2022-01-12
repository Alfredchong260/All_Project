show
databases;
create
database company character set 'utf8mb4';
use
company;

-- 员工信息
create table employee
(
    id      int auto_increment primary key,
    name    varchar(20),
    gender  varchar(2),
    birth   date,
    phone   char(11),
    email   varchar(50),
    address varchar(255),
    id_card char(18)
);
drop table salary;
create table salary
(
    id          int auto_increment primary key,
--     name        varchar(20), -- 还有必要要名字吗? 不用名字应该用什么关联起来
    dept        varchar(20),
    position    varchar(20),
    salary      float,
    employee_id int,
    -- 定义一个外键 外键的名字 关键那个外键 (employee_id) 以那个字段为参考 employee(id)
    constraint fk_user_id foreign key (employee_id) references employee (id)
);

/*
    一对一
    一对多
    多对多
*/

select *
from employee;
select *
from salary;

insert into employee(name, gender, birth, phone, email, address, id_card)
values (%s, %s, %s, %s, %s, %s, %s);
truncate employee;

insert into salary(dept, position, salary, employee_id)
values (%s, %s, %s, %s);

select id
from employee
where name =%s;


/*
    员工表 --> 可以查询名字 --> 可以得到用户id
    薪水表 --> 不能查询名字 --> 可以根据用户id搜索数据


    根据实际的 id 区分人, 名字只是参考的
    如果名字相同可以多条件查询

    ((10, '张三', '生产部门', '18672867241'),(21, '张三', '生产部门', '18672867241'))
*/