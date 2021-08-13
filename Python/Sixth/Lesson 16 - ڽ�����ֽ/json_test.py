'''
什么是json？
    json的类型跟python中的字典长得非常的像但是又不是字典
    例“
        json格式：
        json_str = {"name":"小白","age":20,"like_learning":true,"massage":null}
        python字典格式：
        dict_str = {'name':'小白','age':20,'like_learning':True,'massage':none}

        json_str = {"name":"小白","age":20,"favorit":["python","basketball","run"]}

json在python中的常用方式：
    1.编码(encode)：把一个python对象编码转换成json字符串 json.dumps()
    2.解码(decode)：把json格式字符串解码转换成python对象 json.loadS()
    dumps()  domp是将 Python的数据类型转换为 json
    loads()  load是将 json数据转化为 json

    #认识json
    #json的案例
    #isonpath
    #jsonpath的案例

本堂课重点内容是python的json与jsonpath

    什么是json，什么是jsonpath
        json：
            json  全称 叫做 (JavaScript object Notation)
            json模块提供了四个功能：dumps、dump、loads、load,用于字符串和python数据类型键进行转换。
            json他是用于处理来自任何位置的json数据
            主要有loads()的这个方法
            把json格式字符串解码转换成Python对象从json到Python的类型转化对照如下：
                    json                   python
                    object                 dict
                    array   []               list    []
                    number(int)            int
                    number(float)          float
                    ture                   True
                    false                  False
                    null                   None
            将json转换成 python数据类型使用dumps()
            不得不说json和xml
            相比较json和xml  json的数据类型更加简单明了，采用的是对象和值，也就是说{"name":"小白"}
            我可以通过 name 这个对象 拿到 小白，而xml的体积非常的庞大，不适合轻量级数据交互；

        jsonpath：
            JsonPath是一种信息抽取类库，是从JSON数据中抽取指定信息的工具
            详细参照地址：
                腾讯云博客（jsonpath）：https://cloud.tencent.com/developer/article/1423151
                https://goessner.net/articles/JsonPath/
            《Xpath 》             《 jsonpath》
                /                   $   根节点
                .                   @   现行节点
                /                   .or[]   取子节点
                ..                  n/a 取父节点，Jsonpath未支持
                //                  ..  就是不管位置，选择所有符合条件的条件
                *                   *   匹配所有元素节点
                @                   n/a 根据属性访问，Json不支持，因为Json是个Key-value递归结构，不需要。
                []                  []  迭代器标示（可以在里边做简单的迭代操作，如数组下标，根据内容选值等）
                                    [,] 支持迭代器中做多选。
                []                  ?() 支持过滤操作.
                n/a                 ()  支持表达式计算
                ()                  n/a 分组，JsonPath不支持

            讲解jsonpath的事例；
'''
import json

json_str = '{"name": "chong", "age": 100, "like_learning": true, "massage": null}'
print(type(json_str))

'''
boolean:
    在json中：
        true是小写的,false是小写的
    在python中：
        True是大写的，False是大写的

json的全名是(JavaScrip object Notation)
'''
# json 转字典的操作
dc_str = json.loads(json_str)
print(dc_str)
print(type(dc_str))

dc_test = {'name': '小白', 'age': 100, 'like_learning': True, 'massage': None}

# 将 dict 数据转换成 json 数据：
json_s = json.dumps(dc_test)
print(json_s)
print(type(json_s))