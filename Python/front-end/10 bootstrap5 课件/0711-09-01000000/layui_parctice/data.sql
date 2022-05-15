use python;

create table `student_info`
(
    `id`           int(11)     NOT NULL AUTO_INCREMENT,
    `student_id`   varchar(30) NOT NULL DEFAULT '',
    `student_name` varchar(30) NOT NULL DEFAULT '',
    `email`        varchar(30) NOT NULL DEFAULT '',
    `sex`          varchar(10) NOT NULL DEFAULT '',
    `city`         varchar(30) NOT NULL DEFAULT '',
    `insert_time`  datetime             DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
);
truncate student_info;
insert into student_info (`student_id`, `student_name`, `email`, `sex`, `city`)
values ('000001', '杨斌', 'hejun@example.net', '女', '东市'),
       ('000002', '邓洋', 'xianglei@example.net', '男', '佛山县'),
       ('000003', '刘勇', 'qiujing@example.com', '男', '志强县'),
       ('000004', '王萍', 'qiang72@example.org', '女', '红梅市'),
       ('000005', '李成', 'ldeng@example.net', '女', '西宁市'),
       ('000006', '陈玉华', 'ukong@example.net', '女', '澳门市'),
       ('000007', '谭帆', 'gkong@example.com', '女', '柳州市'),
       ('000008', '张健', 'xiuying93@example.org', '男', '杨县'),
       ('000009', '李楠', 'huangjie@example.org', '男', '兰州市'),
       ('000010', '曾佳', 'yan89@example.com', '男', '北京县'),
       ('000011', '杨桂芳', 'atian@example.com', '女', '淑英市'),
       ('000012', '张红霞', 'xuqiang@example.org', '男', '梧州县'),
       ('000013', '孟桂花', 'sdu@example.net', '女', '石家庄县'),
       ('000014', '欧阳淑兰', 'ugu@example.net', '男', '石家庄县'),
       ('000015', '高萍', 'wenqiang@example.com', '男', '淑珍市'),
       ('000016', '周洁', 'jun39@example.com', '女', '淑兰市'),
       ('000017', '任帆', 'dengxia@example.com', '女', '海燕市'),
       ('000018', '郭玉英', 'cxu@example.net', '女', '桂芝市'),
       ('000019', '钟欢', 'ming06@example.net', '女', '北镇市'),
       ('000020', '姜玉梅', 'ping91@example.net', '女', '玉梅市'),
       ('000021', '岳艳', 'qxie@example.net', '男', '荆门市'),
       ('000022', '李秀云', 'wumin@example.net', '女', '凤英县'),
       ('000023', '黄成', 'ping45@example.net', '男', '凤英市'),
       ('000024', '余婷婷', 'changfang@example.com', '女', '马鞍山县'),
       ('000025', '潘岩', 'taona@example.org', '女', '佳市'),
       ('000026', '李鹏', 'molei@example.com', '男', '勇市'),
       ('000027', '王洁', 'dxie@example.com', '男', '丽娟县'),
       ('000028', '孙雪', 'uyan@example.org', '女', '宁德县'),
       ('000029', '徐莹', 'liangguiying@example.com', '女', '秀兰市'),
       ('000030', '杨丹', 'chaosu@example.net', '男', '南京县');


select *
from student_info;


select *
from student_info
where student_name like '%飞%';

DELETE FROM student_info WHERE id='';
UPDATE student_info SET email='',列2=值2 WHERE id='';