def func(*args, **kwargs):
    """
    :param args: 接受位置参数
    :param kwargs: 接受关键字参数
    :return:
    """
    print('args:\t', args)
    print('kwargs:\t', kwargs)


# 关键字参数后面只能是关键字参数
# 传递参数只能传关键字参数与位置参数
func(1, 2, 3, 4, five=5, six=6, seven=7)
"""
    不学这些东西,怎么把别人的想法变成代码
"""
