import queue
import threading
import time


def producer(pipeline):
    """生成者 厨师做包子"""
    index = 1
    while True:
        time.sleep(0.3)
        print(f'厨师做出了第{index}包子')
        pipeline.put(f'第{index}个包子')
        index += 1


def consumer(pipeline):
    """消费者"""
    while True:
        time.sleep(0.1)
        message = pipeline.get()
        print('消费者吃掉了' + message)


# 1. 定义一个队列用于存储数据
pipe = queue.Queue(19)
# 2.1 生产者随时可能生成数据
t1 = threading.Thread(target=producer, args=(pipe,))
t1.start()
time.sleep(3)
# 2.2 消费者可能随时消费数据
t2 = threading.Thread(target=consumer, args=(pipe,))
t2.start()

# 99 error 99 warning
