"""
创建一个函数`Example`

实例属性：
​	.list_1 将 `['1','2','3','4']` 变为数字数组
​	.list_2  将 `'5678'` 变为数字数组

实例方法：
​	.list_map 分别返回两个列表（列表里面都是数字）
​	.list_map_sort 分别逆序返回两个列表（列表里面都是数字）
​	.list_max 分别返回两个列表中的最大值
​	.list_sum 分别返回两个列表的和
​	.list_filter 分别返回两个列表中的偶数位
​	.list_zip 将两个列表合并后返回
​	.list_to_dict 将两个列表变成字典返回，list_1 作为键 list_2 作为值
​	.list_1_set 将此类方法设置为属性，访问是用过 `对象.list_1_set = [0,0,0,0]` 就可以修改 `self.list_1` 的值
"""


class Example:
    def __init__(self):
        self.list_1 = ['1', '2', '3', '4']
        self.list_2 = '5678'

    # 分别返回两个列表（列表里面都是数字）
    def list_map(self):
        list1 = list(map(int, self.list_1))
        list2 = list(map(int, self.list_2))
        return list1, list2

    # 分别逆序返回两个列表（列表里面都是数字）
    def list_map_sort(self):
        list1, list2 = self.list_map()
        lst1 = sorted(list1, reverse=True)
        lst2 = sorted(list2, reverse=True)
        return lst1, lst2

    # 分别返回两个列表中的最大值
    def list_max(self):
        list1, list2 = self.list_map()
        max1 = max(list1)
        max2 = max(list2)
        print("列表1的最大值为{}".format(max1))
        print("列表2的最大值为{}".format(max2))
        return max1, max2

    # 分别返回两个列表的和
    def list_sum(self):
        list1, list2 = self.list_map()
        sum1 = sum(list1)
        sum2 = sum(list2)
        print("列表1的和为{}".format(sum1))
        print("列表2的和为{}".format(sum2))
        return sum1, sum2

    # 分别返回两个列表中的偶数位
    def list_filter(self):
        list1, list2 = self.list_map()
        list1 = list(filter(lambda x: x % 2 == 0, list1))
        list2 = list(filter(lambda x: x % 2 == 0, list2))
        return list1, list2

    # 将两个列表合并后返回
    def list_zip(self):
        list1, list2 = self.list_map()
        list_merge = list(zip(list1,list2))
        return list_merge

    # 将两个列表变成字典返回，list_1 作为健 list_2 作为指
    def list_to_dict(self):
        list1, list2 = self.list_map()
        dict12 = dict(zip(list1, list2))
        return dict12

    # 将此类方法设置为属性，访问是用过 `对象.list_1_set = [0,0,0,0]` 就可以修改 `list_1` 的值
    @property
    def list_1_set(self):
        return self.list_1

    # 可以用等于符号对特性进行操作
    @list_1_set.setter
    def list_1_set(self, value):
        self.list_1 = value

    @list_1_set.deleter
    def list_1_set(self):
        del self.list_1


if __name__ == '__main__':
    e = Example()
    print(e.list_map())
    print('-'*30)
    print(e.list_map_sort())
    print('-' * 30)
    print(e.list_max())
    print('-' * 30)
    print(e.list_sum())
    print('-' * 30)
    print(e.list_filter())
    print('-' * 30)
    print(e.list_zip())
    print('-' * 30)
    print(e.list_to_dict())
    print('-' * 30)
    print(e.list_1_set)
    e.list_1_set = [0, 0, 0, 0]
    print('-' * 30)
    print(e.list_1_set)
