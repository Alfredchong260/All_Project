# """
#     temp列表在这里到底起什么作用啊
#     print(sorted(tuple(arr), key=lambda temp: temp[0] + temp[1]))
#
#     选择大于努力
# """
#
# arr = [(1, 2), (4, 1), (9, 10), (13, -3)]
# arr2 = [5, 3, -3, 9, 5, -5, 7, -1]
#
#
# def func(temp):
#     print('排序规则:', temp)
#     return abs(temp[0]) + abs(temp[1])
#
#
# # key 只是排序规则,不会修改原有的数据
# arr.sort(key=func)  # arr2 里面元素的绝对值进行排序
#
# print(arr)

"""
可以讲下 threading 任务定时吗

定时任务
    语言级别的定时任务

工作过程中定时任务
    corntab             linux 定时任务,系统级别
    supervisor          linux 守护进行,系统级别
"""

