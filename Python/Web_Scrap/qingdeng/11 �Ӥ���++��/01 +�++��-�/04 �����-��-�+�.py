import time
import threading  # 线程模块, 内置模块


def sing():
    for i in range(3):
        print(f'正在唱歌...{i}')
        time.sleep(1)


def dance():
    for i in range(3):
        print(f'正在跳舞...{i}')
        time.sleep(1)

sing_thread = threading.Thread(target=sing).start()
dance_thread = threading.Thread(target=dance).start()
print('主线程执行到这里了...')


"""
主线程会先执行完, 并不意味着主线程会跟着跑路
主线程执行完以后, 会等待子线程执行任务, 直到任务执行完毕
"""
