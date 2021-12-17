import time


# def my_range(start, stop, step):
#     ret = []
#     current = start
#     while current <= stop:
#         # return 默认只能返回一次
#         # 爬虫请求10页面
#         time.sleep(0.5)
#         ret.append(current)
#         current += step
#     return ret

def my_range(start, stop, step):
    current = start
    while current <= stop:
        # yield 生产,生成,生成器
        time.sleep(0.5)
        yield f'http://www.maoyan.com?page={current}'
        current += step


# generator 生成器 会提前返回生成器对象,
# [0,1,2,3,4,5,6,7,8,9]
ret = my_range(0, 10, 1)
print('ret:\t', ret)
for item in ret:
    print(item)
