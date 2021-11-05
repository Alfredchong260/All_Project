import threading
import time
import random


def add1(n):

    for i in range(100):
        time.sleep(random.randint(1, 3))  # 函数的随机等待, 程序挂起
        with open('hello.txt', mode='a', encoding='utf-8') as f:
            f.write(f'{n} hello world !' + 'hello world !' * 1024)
            f.write('\n')


if __name__ == '__main__':
    for n in range(10):
        t1 = threading.Thread(target=add1, args=(n,))
        t1.start()



# 多任务没有绝对执行顺序:   只有逻辑顺序


# 多任务资源竞争
# 多线程: 每一个线程做事非常积极, 会抢着做任务, 有可能引发资源竞争, 出现我们不想要的结果