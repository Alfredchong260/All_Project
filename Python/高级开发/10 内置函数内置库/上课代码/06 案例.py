score = [('9.', '1'), ('8.', '8'),
         ('9.', '0'), ('9.', '0'),
         ('9.', '0'), ('8.', '9'),
         ('9.', '1'), ('9.', '3'),
         ('9.', '3'), ('9.', '2')]

name = ['龙猫', '阿飞正传', '爱·回家', '海洋', '我爱你', '黄金三镖客', '迁徙的鸟', '千与千寻', '海上钢琴师', '天堂电影院']

# 所有的高级函数处理的都是可迭代对象
# 把分数合并
score = map(lambda temp: temp[0] + temp[1], score)  # 返回的是一个生成器对象
score = map(float, score)
# print(list(score))
# print(list(score))
# print(list(score))  # 第二次强制转化没有结果,生成器对象只能强制转化一次
# 把名字与分数合并
info = zip(name, score)
# 筛选 9.0 分以上的电影
# for + if --> filter
info = filter(lambda temp: temp[1] > 9.0, info)
print(list(sorted(info, key=lambda temp: temp[1], reverse=True)))


# print(list(
#     sorted(zip(name, map(float, map(lambda temp: temp[0] + temp[1], score))),
#            key=lambda temp: temp[1], reverse=True)))
"""
    for
    函数式编程
    嵌套的函数式编程
"""
