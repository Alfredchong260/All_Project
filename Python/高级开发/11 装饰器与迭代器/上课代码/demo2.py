import time


# 之前编写的计算时间的装饰函数
def wrapper_func(target_func):
    def wrapper(*args, **kwargs):
        """装饰的逻辑"""
        # *args, **kwargs 函数的位置参数全部接受与关键字参数
        start_time = time.time()
        # print('target_func', target_func, '\nargs:\t', args)
        result = target_func(*args, **kwargs)  # 然后再将参数传递给真正执行的函数
        # print('运行的时间:\t', time.time() - start_time)
        open('time.txt', mode='w', encoding='utf-8').write('运行的时间:\t' + str(time.time() - start_time))
        return result

    return wrapper  # 把装饰函数返回出去


# 计算 input 数据用了多少是时间?
# input = wrapper_func(input)
#
# ret = input('请输入任意个参数')
# print(ret)

print = wrapper_func(print)
# 你调用 print 的时候会传递多少个参数?
print(1, 2, 3, end='\n', sep='\t')
