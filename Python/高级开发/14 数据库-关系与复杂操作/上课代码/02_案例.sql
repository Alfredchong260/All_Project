/*
('丁娜','销售部门','女','1998/12/27','18706012232','532211428@qq.com','北京市海淀区颐和园路5号','342622199801144314'),
('陈伟','生产部门','男','1995/10/25','13459732456','572501101@qq.com','北京市海淀区双清路30号','342622199709066819'),
('曲旭','销售部门','男','1999/1/8','18850840171','582300330@qq.com','上海市杨浦区邯郸路220号','342622199709198176'),
('刘淑珍','销售部门','女','1998/2/4','18650523989','588100505@qq.com','杭州市西湖区余杭塘路866号','342622199708171596'),
('王晶','生产部门','男','1998/4/20','18650795182','598202702@qq.com','上海市杨浦区四平路1239号','342622199711026453'),
('刘红梅','技术部','女','1998/7/20','18759125223','512101504@qq.com','厦门市思明区思明南路422号','320923199806290932'),
('陈秀兰','技术部','男','1999/2/1','18705908359','512501129@qq.com','江苏省南京市鼓楼区汉口路22号','342625199812140158'),
('戴文','技术部','男','1997/1/15','18065178692','512802414@qq.com','重庆市沙坪坝区沙坪坝正街174号','342601199705132151'),
('陈丽','技术部','女','1998/11/29','15260972133','518110817@qq.com','四川省成都市武侯区一环路南一段24号','340223199802050515'),
('冉兵','技术部','男','1997/9/15','13850208664','530300603@qq.com','广州市海珠区新港西路135号','342623199806105732'),
*/

use dzdp;
drop table employee;
create table employee
(
    id      int primary key auto_increment,
    name    varchar(255)        not null comment '姓名',
    dept    varchar(20) comment '部门',
    gender  char(2) default '女' not null comment '性别',
    birth   date                not null comment '出生日期',
    phone   char(11)            not null unique comment '电话号码',
    email   varchar(255) comment '邮箱',
    address varchar(255)        not null comment '地址',
    id_card char(18)            not null unique comment '身份证号码'
);

desc employee;
show create table employee; -- 查看数据表的创建语句
show index from employee; -- 查看数据表的创建语句

/*

CREATE TABLE `employee` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL COMMENT '姓名',
  `dept` varchar(20) DEFAULT NULL COMMENT '部门',
  `gender` char(2) NOT NULL DEFAULT '女' COMMENT '性别',
  `birth` date NOT NULL COMMENT '出生日期',
  `phone` char(11) NOT NULL COMMENT '电话号码',
  `email` varchar(255) DEFAULT NULL COMMENT '邮箱',
  `address` varchar(255) NOT NULL COMMENT '地址',
  `id_card` char(18) NOT NULL COMMENT '身份证号码',
  PRIMARY KEY (`id`),
  UNIQUE KEY `phone` (`phone`),
  UNIQUE KEY `id_card` (`id_card`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
*/

/*
varchar(3)  最长容纳3个字符
varchar(20) 最长容纳20个字符  根据实际存储的内容占据空间
char(3)     固定容纳3个字符
*/