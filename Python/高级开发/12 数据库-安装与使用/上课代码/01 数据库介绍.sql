/*
    开发环境(windows): phpstudy 安装使用简单
    生成环境(linux): 可以给所有的人使用

    excel(office,wps)                sql(mysql,sqlite,sql server....)
    maoyan.xlsx                      数据库(database)
    sheet 表                         数据表(tables)
    数据列                            字段
    数据行                            记录
*/
show databases;

-- 1. 打开数据库
-- 创建数据库
create database python character set 'utf8mb4';
-- utf8mb4 是为了兼容 emoji图片,
-- 如果不是 utf8 编码,不能存中文内容
-- 删除数据库
drop database python;


-- 创建数据表
use python; -- 使用数据库
show tables ;



use mysql;
show tables ;
desc user;
select * from user;