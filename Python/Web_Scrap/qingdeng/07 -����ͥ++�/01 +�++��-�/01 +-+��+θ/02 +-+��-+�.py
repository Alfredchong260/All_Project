"""
.read()     读取打开文件的所有数据
readline()  读取文件的一行数据(适合大文件的读取)
readlines() 读取文件的所有数据, 返回一个列表, 每一行都是列表里面单独一个元素
"""

with open('hello.txt', mode='r', encoding='utf-8') as f:
    # txt = f.read()
    # print(txt)

    # while True:
    #     txt = f.readline()
    #     """在循环中读取出来的每一行数据可以写每一行数据的代码逻辑"""
    #     print(txt)
    #     if txt == '':
    #         break

    txt = f.readlines()
    print(txt)