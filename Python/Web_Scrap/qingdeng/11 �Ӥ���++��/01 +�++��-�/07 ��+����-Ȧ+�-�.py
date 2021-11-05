import threading
import time
import random

# 创建一把锁
lock = threading.Lock()


def add1(n):

    for i in range(100):
        time.sleep(random.randint(1, 3))

        lock.acquire()  # 上锁
        with open('hello.txt', mode='a', encoding='utf-8') as f:
            f.write(f'{n} hello world !' + 'hello world !' * 1024)
            f.write('\n')
        # 上万所以后一定要记得解锁, 不然会出现死锁<引发报错>
        lock.release()  # 解锁

if __name__ == '__main__':
    for n in range(10):
        t1 = threading.Thread(target=add1, args=(n,))
        t1.start()


"""
什么情况下上锁?
    对一个文件多次使用多任务操作
    全局变量进行多任务运算
    
    
加锁:
    只要锁住关键代码就可以了, 因为如果一旦上锁, 那么只有一个任务在执行的时候能够拿到这把锁
    加锁不要在全部代码中加锁
"""

