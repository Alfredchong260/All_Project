import sys
import time


# def progress_bar():
#     for i in range(1, 101):
#         print("\r", end="")
#         print("Download progress: {}%: ".format(i), "▋" * (i // 2), end="")
#         sys.stdout.flush()
#         time.sleep(0.05)

# if __name__ == '__main__':
#     progress_bar()

# def toolBar():
#     list_bat = (range(1000000))
#     count = 0

#     with open("./hello.txt", 'w') as f:
#         for i in list_bat:
#             f.write(str(i))
#             count += 1
            
#             print("\r当前速度：{:.2f}%".format(count * 100 / len(list_bat)), end="")

# if __name__ == "__main__":
#     toolBar()
# !/user/bin/env python
# -*- coding:utf-8 -*-
 
import time
from tqdm import tqdm
from tqdm._tqdm import trange
 
for i in tqdm(range(1000)):
    time.sleep(0.03)
