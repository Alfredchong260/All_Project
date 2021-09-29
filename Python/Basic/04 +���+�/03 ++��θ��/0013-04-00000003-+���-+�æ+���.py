"""
作业2：
运行代码之后，请找出下面代码错误并且修正

提示：深浅拷贝
"""

from pprint import pprint
import copy

data = {
    'cate': '童书馆',
    'sub_cate': None
}
sub_cate = ['科普百科', '儿童文学', '幼儿启蒙', '动漫卡通', '少儿英语']

all_cate = []

for cate in sub_cate:
    data1 = copy.copy(data)
    data1['sub_cate'] = cate
    all_cate.append(data1)


pprint(all_cate)
