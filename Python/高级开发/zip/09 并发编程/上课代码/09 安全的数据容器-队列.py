import queue

# 1. 定义队列
q = queue.Queue(maxsize=10)  # maxsize 最大同时容纳10条数据
print('队列目前的容量:', q.qsize())
for index in range(1, 11):
    q.put(f'第{index}个包子')  # put 往队列里面添加内容

# print('队列目前的容量:', q.qsize())
# q.put(f'第11个包子')  # 最大容量为 10, 当放不进去的时候就会等待有空间的时候再放进去

while q.qsize() >= 1:
    print('吃掉:\t', q.get())  # get 获取队列里面的内容
print('吃掉:\t', q.get())  # 队列里面没有内容的时候,会阻塞等待有数据

# get put 操作里面已经加锁了
