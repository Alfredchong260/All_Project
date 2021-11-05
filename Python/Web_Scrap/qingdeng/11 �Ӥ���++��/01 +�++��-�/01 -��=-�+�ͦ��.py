import time


def sing():
    for i in range(3):
        print(f'正在唱歌...{i}')
        time.sleep(1)


def dance():
    for i in range(3):
        print(f'正在跳舞...{i}')
        time.sleep(1)

start_time = time.time()

sing()
dance()

print('执行任务花费时间: ', time.time() - start_time)


# 程序的等待,意味着程序是阻塞的, 或者说是挂起的
# 单线程