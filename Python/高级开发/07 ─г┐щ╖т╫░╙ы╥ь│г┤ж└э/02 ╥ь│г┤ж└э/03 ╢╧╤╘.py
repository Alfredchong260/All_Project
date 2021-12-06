def str_2_number(str_):
    """字符串转数字"""
    # 如果字符串不是数字就会报错
    # if not str_.isdigit():  # isdigit 判断是不是数字字符串 '123' 'a123'
    #     # 如果不是字符串数字,后面转化的时候就会报错
    #     raise Exception('请传入一个字符串类型')

    # 断言  表达式(必须返回布尔类型), 如果不符合条件的报错
    assert str_.isdigit(), Exception('请传入一个字符串类型')

    number = int(str_)
    return number


num = str_2_number('2')
print(num)
print(type(num))

"""
    raise : 主动抛出错误,程序会接受(手动在程序内部结束程序)

"""
