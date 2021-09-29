

"""
file         打开文件的路径(绝对路径/相对路径)

mode         文件操作的模式(指定字符串)
                w  write  写入  每次写数据之前, 首先都会清空所有数据
                r  read   读取
                a  append 追加数据   每次写数据, 都是在文件原有数据的尾部写入
                b  binary 二进制数据(图片, 视频, 音频)

encoding      文件编码, utf-8 万国码<linux 系统>  gbk<windows系统下默认的编码格式>
"""

# 打开了一个文件
file = open('hello.txt', mode='a')

# 操作文件, write() **只能写入字符串和二进制数据**
file.write('hello python!')
# file.write(123)
# file.write([123])

# 关闭文件
file.close()

