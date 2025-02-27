/*
    数据库地址: 159.75.114.202
    数据库用户名: windows
    数据库密码: 123456

    1. 在远程数据库服务器中创建一个属于自己的数据库：16_00_正心（作业次数-学号-名字）
    2. 选择数据库后创建一张 douban 数据表（id, movie_name, other_name, info, score, follows）
    3. 将处理后的 douban.csv 数据插入到数据库


    ps:
    (.*?),(.*?),(.*?),(.*?),(.*)
    ("$1","$2","$3","$4","$5"),
*/

show databases;

create database 16_00_zx character set 'utf8mb4';

use 16_00_zx;
drop table douban;
create table douban
(
    id         int primary key auto_increment,
    movie_name varchar(255),
    other_name varchar(255),
    info       text,
    score      float,
    follows    int # 数字占用的空间会更小
);

desc douban;

insert into douban(movie_name, other_name, info, score, follows)
values ("肖申克的救赎","肖申克的救赎/ The Shawshank Redemption/ 月黑高飞(港)  /  刺激1995(台)","导演: 弗兰克·德拉邦特 Frank Darabont   主演: 蒂姆·罗宾斯 Tim Robbins /...1994 / 美国 / 犯罪 剧情","9.7","1981964"),
("霸王别姬","霸王别姬/ 再见，我的妾  /  Farewell My Concubine","导演: 陈凯歌 Kaige Chen   主演: 张国荣 Leslie Cheung / 张丰毅 Fengyi Zha...1993 / 中国大陆 中国香港 / 剧情 爱情 同性","9.6","1466594"),
("阿甘正传","阿甘正传/ Forrest Gump/ 福雷斯特·冈普","导演: 罗伯特·泽米吉斯 Robert Zemeckis   主演: 汤姆·汉克斯 Tom Hanks / ...1994 / 美国 / 剧情 爱情","9.5","1502559"),
("这个杀手不太冷","这个杀手不太冷/ Léon/ 杀手莱昂  /  终极追杀令(台)","导演: 吕克·贝松 Luc Besson   主演: 让·雷诺 Jean Reno / 娜塔莉·波特曼 ...1994 / 法国 / 剧情 动作 犯罪","9.4","1696348"),
("美丽人生","美丽人生/ La vita è bella/ 一个快乐的传说(港)  /  Life Is Beautiful","导演: 罗伯托·贝尼尼 Roberto Benigni   主演: 罗伯托·贝尼尼 Roberto Beni...1997 / 意大利 / 剧情 喜剧 爱情 战争","9.5","947714"),
("泰坦尼克号","泰坦尼克号/ Titanic/ 铁达尼号(港 / 台)","导演: 詹姆斯·卡梅隆 James Cameron   主演: 莱昂纳多·迪卡普里奥 Leonardo...1997 / 美国 / 剧情 爱情 灾难","9.4","1450471"),
("千与千寻","千与千寻/ 千と千尋の神隠し/ 神隐少女(台)  /  千与千寻的神隐","导演: 宫崎骏 Hayao Miyazaki   主演: 柊瑠美 Rumi Hîragi / 入野自由 Miy...2001 / 日本 / 剧情 动画 奇幻","9.4","1551806"),
("辛德勒的名单","辛德勒的名单/ Schindler's List/ 舒特拉的名单(港)  /  辛德勒名单","导演: 史蒂文·斯皮尔伯格 Steven Spielberg   主演: 连姆·尼森 Liam Neeson...1993 / 美国 / 剧情 历史 战争","9.5","766569"),
("盗梦空间","盗梦空间/ Inception/ 潜行凶间(港)  /  全面启动(台)","导演: 克里斯托弗·诺兰 Christopher Nolan   主演: 莱昂纳多·迪卡普里奥 Le...2010 / 美国 英国 / 剧情 科幻 悬疑 冒险","9.3","1440335"),
("忠犬八公的故事","忠犬八公的故事/ Hachi: A Dog's Tale/ 忠犬小八(台)  /  秋田犬八千(港)","导演: 莱塞·霍尔斯道姆 Lasse Hallström   主演: 理查·基尔 Richard Ger...2009 / 美国 英国 / 剧情","9.4","996903"),
("海上钢琴师","海上钢琴师/ La leggenda del pianista sull'oceano/ 声光伴我飞(港)  /  一九零零的传奇","导演: 朱塞佩·托纳多雷 Giuseppe Tornatore   主演: 蒂姆·罗斯 Tim Roth / ...1998 / 意大利 / 剧情 音乐","9.3","1199518"),
("楚门的世界","楚门的世界/ The Truman Show/ 真人Show(港)  /  真人戏","导演: 彼得·威尔 Peter Weir   主演: 金·凯瑞 Jim Carrey / 劳拉·琳妮 Lau...1998 / 美国 / 剧情 科幻","9.3","1063777"),
("三傻大闹宝莱坞","三傻大闹宝莱坞/ 3 Idiots/ 三个傻瓜(台)  /  作死不离3兄弟(港)","导演: 拉库马·希拉尼 Rajkumar Hirani   主演: 阿米尔·汗 Aamir Khan / 卡...2009 / 印度 / 剧情 喜剧 爱情 歌舞","9.2","1331035"),
("机器人总动员","机器人总动员/ WALL·E/ 瓦力(台)  /  太空奇兵·威E(港)","导演: 安德鲁·斯坦顿 Andrew Stanton   主演: 本·贝尔特 Ben Burtt / 艾丽...2008 / 美国 / 科幻 动画 冒险","9.3","949831"),
("放牛班的春天","放牛班的春天/ Les choristes/ 歌声伴我心(港)  /  唱诗班男孩","导演: 克里斯托夫·巴拉蒂 Christophe Barratier   主演: 热拉尔·朱尼奥 Gé...2004 / 法国 瑞士 德国 / 剧情 音乐","9.3","926485"),
("星际穿越","星际穿越/ Interstellar/ 星际启示录(港)  /  星际效应(台)","导演: 克里斯托弗·诺兰 Christopher Nolan   主演: 马修·麦康纳 Matthew Mc...2014 / 美国 英国 加拿大 冰岛 / 剧情 科幻 冒险","9.3","1070232"),
("大话西游之大圣娶亲","大话西游之大圣娶亲/ 西遊記大結局之仙履奇緣/ 西游记完结篇仙履奇缘  /  齐天大圣西游记","导演: 刘镇伟 Jeffrey Lau   主演: 周星驰 Stephen Chow / 吴孟达 Man Tat Ng...1995 / 中国香港 中国大陆 / 喜剧 爱情 奇幻 古装","9.2","1048846"),
("熔炉","熔炉/ 도가니/ 无声呐喊(港)  /  漩涡","导演: 黄东赫 Dong-hyuk Hwang   主演: 孔侑 Yoo Gong / 郑有美 Yu-mi Jung /...2011 / 韩国 / 剧情","9.3","645266"),
("疯狂动物城","疯狂动物城/ Zootopia/ 优兽大都会(港)  /  动物方城市(台)","导演: 拜伦·霍华德 Byron Howard / 瑞奇·摩尔 Rich Moore   主演: 金妮弗·...2016 / 美国 / 喜剧 动画 冒险","9.2","1248940"),
("无间道","无间道/ 無間道/ Infernal Affairs  /  Mou gaan dou","导演: 刘伟强 / 麦兆辉   主演: 刘德华 / 梁朝伟 / 黄秋生2002 / 中国香港 / 剧情 犯罪 悬疑","9.2","854051"),
("龙猫","龙猫/ となりのトトロ/ 邻居托托罗  /  邻家的豆豆龙","导演: 宫崎骏 Hayao Miyazaki   主演: 日高法子 Noriko Hidaka / 坂本千夏 Ch...1988 / 日本 / 动画 奇幻 冒险","9.2","891717"),
("教父","教父/ The Godfather/ Mario Puzo's The Godfather","导演: 弗朗西斯·福特·科波拉 Francis Ford Coppola   主演: 马龙·白兰度 M...1972 / 美国 / 剧情 犯罪","9.3","651518"),
("当幸福来敲门","当幸福来敲门/ The Pursuit of Happyness/ 寻找快乐的故事(港)  /  追求快乐","导演: 加布里尔·穆奇诺 Gabriele Muccino   主演: 威尔·史密斯 Will Smith ...2006 / 美国 / 剧情 传记 家庭","9.1","1064740"),
("怦然心动","怦然心动/ Flipped/ 萌动青春  /  青春萌动","导演: 罗伯·莱纳 Rob Reiner   主演: 玛德琳·卡罗尔 Madeline Carroll / 卡...2010 / 美国 / 剧情 喜剧 爱情","9.1","1235529"),
("触不可及","触不可及/ Intouchables/ 闪亮人生(港)  /  逆转人生(台)","导演: 奥利维·那卡什 Olivier Nakache / 艾力克·托兰达 Eric Toledano   主...2011 / 法国 / 剧情 喜剧","9.2","696019"),
("肖申克的救赎","肖申克的救赎/ The Shawshank Redemption/ 月黑高飞(港)  /  刺激1995(台)","导演: 弗兰克·德拉邦特 Frank Darabont   主演: 蒂姆·罗宾斯 Tim Robbins /...1994 / 美国 / 犯罪 剧情","9.7","1989087"),
("霸王别姬","霸王别姬/ 再见，我的妾  /  Farewell My Concubine","导演: 陈凯歌 Kaige Chen   主演: 张国荣 Leslie Cheung / 张丰毅 Fengyi Zha...1993 / 中国大陆 中国香港 / 剧情 爱情 同性","9.6","1472240"),
("阿甘正传","阿甘正传/ Forrest Gump/ 福雷斯特·冈普","导演: 罗伯特·泽米吉斯 Robert Zemeckis   主演: 汤姆·汉克斯 Tom Hanks / ...1994 / 美国 / 剧情 爱情","9.5","1507339"),
("这个杀手不太冷","这个杀手不太冷/ Léon/ 杀手莱昂  /  终极追杀令(台)","导演: 吕克·贝松 Luc Besson   主演: 让·雷诺 Jean Reno / 娜塔莉·波特曼 ...1994 / 法国 / 剧情 动作 犯罪","9.4","1701191"),
("美丽人生","美丽人生/ La vita è bella/ 一个快乐的传说(港)  /  Life Is Beautiful","导演: 罗伯托·贝尼尼 Roberto Benigni   主演: 罗伯托·贝尼尼 Roberto Beni...1997 / 意大利 / 剧情 喜剧 爱情 战争","9.5","950417"),
("泰坦尼克号","泰坦尼克号/ Titanic/ 铁达尼号(港 / 台)","导演: 詹姆斯·卡梅隆 James Cameron   主演: 莱昂纳多·迪卡普里奥 Leonardo...1997 / 美国 / 剧情 爱情 灾难","9.4","1456632"),
("千与千寻","千与千寻/ 千と千尋の神隠し/ 神隐少女(台)  /  千与千寻的神隐","导演: 宫崎骏 Hayao Miyazaki   主演: 柊瑠美 Rumi Hîragi / 入野自由 Miy...2001 / 日本 / 剧情 动画 奇幻","9.4","1557730"),
("辛德勒的名单","辛德勒的名单/ Schindler's List/ 舒特拉的名单(港)  /  辛德勒名单","导演: 史蒂文·斯皮尔伯格 Steven Spielberg   主演: 连姆·尼森 Liam Neeson...1993 / 美国 / 剧情 历史 战争","9.5","769011"),
("盗梦空间","盗梦空间/ Inception/ 潜行凶间(港)  /  全面启动(台)","导演: 克里斯托弗·诺兰 Christopher Nolan   主演: 莱昂纳多·迪卡普里奥 Le...2010 / 美国 英国 / 剧情 科幻 悬疑 冒险","9.3","1444430"),
("忠犬八公的故事","忠犬八公的故事/ Hachi: A Dog's Tale/ 忠犬小八(台)  /  秋田犬八千(港)","导演: 莱塞·霍尔斯道姆 Lasse Hallström   主演: 理查·基尔 Richard Ger...2009 / 美国 英国 / 剧情","9.4","1000786"),
("海上钢琴师","海上钢琴师/ La leggenda del pianista sull'oceano/ 声光伴我飞(港)  /  一九零零的传奇","导演: 朱塞佩·托纳多雷 Giuseppe Tornatore   主演: 蒂姆·罗斯 Tim Roth / ...1998 / 意大利 / 剧情 音乐","9.3","1203219"),
("楚门的世界","楚门的世界/ The Truman Show/ 真人Show(港)  /  真人戏","导演: 彼得·威尔 Peter Weir   主演: 金·凯瑞 Jim Carrey / 劳拉·琳妮 Lau...1998 / 美国 / 剧情 科幻","9.3","1067737"),
("三傻大闹宝莱坞","三傻大闹宝莱坞/ 3 Idiots/ 三个傻瓜(台)  /  作死不离3兄弟(港)","导演: 拉库马·希拉尼 Rajkumar Hirani   主演: 阿米尔·汗 Aamir Khan / 卡...2009 / 印度 / 剧情 喜剧 爱情 歌舞","9.2","1335526"),
("机器人总动员","机器人总动员/ WALL·E/ 瓦力(台)  /  太空奇兵·威E(港)","导演: 安德鲁·斯坦顿 Andrew Stanton   主演: 本·贝尔特 Ben Burtt / 艾丽...2008 / 美国 / 科幻 动画 冒险","9.3","952523"),
("放牛班的春天","放牛班的春天/ Les choristes/ 歌声伴我心(港)  /  唱诗班男孩","导演: 克里斯托夫·巴拉蒂 Christophe Barratier   主演: 热拉尔·朱尼奥 Gé...2004 / 法国 瑞士 德国 / 剧情 音乐","9.3","929604"),
("星际穿越","星际穿越/ Interstellar/ 星际启示录(港)  /  星际效应(台)","导演: 克里斯托弗·诺兰 Christopher Nolan   主演: 马修·麦康纳 Matthew Mc...2014 / 美国 英国 加拿大 冰岛 / 剧情 科幻 冒险","9.3","1073862"),
("大话西游之大圣娶亲","大话西游之大圣娶亲/ 西遊記大結局之仙履奇緣/ 西游记完结篇仙履奇缘  /  齐天大圣西游记","导演: 刘镇伟 Jeffrey Lau   主演: 周星驰 Stephen Chow / 吴孟达 Man Tat Ng...1995 / 中国香港 中国大陆 / 喜剧 爱情 奇幻 古装","9.2","1053145"),
("熔炉","熔炉/ 도가니/ 无声呐喊(港)  /  漩涡","导演: 黄东赫 Dong-hyuk Hwang   主演: 孔侑 Yoo Gong / 郑有美 Yu-mi Jung /...2011 / 韩国 / 剧情","9.3","648040"),
("疯狂动物城","疯狂动物城/ Zootopia/ 优兽大都会(港)  /  动物方城市(台)","导演: 拜伦·霍华德 Byron Howard / 瑞奇·摩尔 Rich Moore   主演: 金妮弗·...2016 / 美国 / 喜剧 动画 冒险","9.2","1253845"),
("无间道","无间道/ 無間道/ Infernal Affairs  /  Mou gaan dou","导演: 刘伟强 / 麦兆辉   主演: 刘德华 / 梁朝伟 / 黄秋生2002 / 中国香港 / 剧情 犯罪 悬疑","9.2","857182"),
("龙猫","龙猫/ となりのトトロ/ 邻居托托罗  /  邻家的豆豆龙","导演: 宫崎骏 Hayao Miyazaki   主演: 日高法子 Noriko Hidaka / 坂本千夏 Ch...1988 / 日本 / 动画 奇幻 冒险","9.2","894378"),
("教父","教父/ The Godfather/ Mario Puzo's The Godfather","导演: 弗朗西斯·福特·科波拉 Francis Ford Coppola   主演: 马龙·白兰度 M...1972 / 美国 / 剧情 犯罪","9.3","653392"),
("当幸福来敲门","当幸福来敲门/ The Pursuit of Happyness/ 寻找快乐的故事(港)  /  追求快乐","导演: 加布里尔·穆奇诺 Gabriele Muccino   主演: 威尔·史密斯 Will Smith ...2006 / 美国 / 剧情 传记 家庭","9.1","1067997"),
("怦然心动","怦然心动/ Flipped/ 萌动青春  /  青春萌动","导演: 罗伯·莱纳 Rob Reiner   主演: 玛德琳·卡罗尔 Madeline Carroll / 卡...2010 / 美国 / 剧情 喜剧 爱情","9.1","1240055"),
("触不可及","触不可及/ Intouchables/ 闪亮人生(港)  /  逆转人生(台)","导演: 奥利维·那卡什 Olivier Nakache / 艾力克·托兰达 Eric Toledano   主...2011 / 法国 / 剧情 喜剧","9.2","698494");

select * from douban;

truncate douban;
use python;
drop table student;