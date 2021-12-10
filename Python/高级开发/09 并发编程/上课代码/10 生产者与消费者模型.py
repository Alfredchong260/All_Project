import queue
import threading
import time


def producer(pipeline):
    """生成者 厨师做包子"""
    # 什么时候会进行点赞投币, 点赞投币会产生信息
    index = 1
    while True:
        time.sleep(0.3)
        print(f'厨师做出了第{index}包子')
        pipeline.put(f'第{index}个包子')
        index += 1


def consumer(pipeline):  # pipeline 用于传输数据的队列
    """消费者"""
    # up 主什么时候会 消费信息
    while True:
        time.sleep(0.1)
        message = pipeline.get()
        print('消费者吃掉了' + message)


# 存储数据的队列要不要限制大小,以及限制多大
pipe = queue.Queue(19)  # 主要是用来传输数据的 提前准备好数据容器队列(类似列表)
t1 = threading.Thread(target=producer, args=(pipe,))
t1.start()
time.sleep(3)
t2 = threading.Thread(target=consumer, args=(pipe,))
t2.start()
