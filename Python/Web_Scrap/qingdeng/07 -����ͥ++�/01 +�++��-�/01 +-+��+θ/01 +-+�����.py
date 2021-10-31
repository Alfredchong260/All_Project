

# 文件尾缀: 是给软件识别  .mp3
# a 追加: 在文件尾部追加数据
# w 写入: 首先会清空当前那文件所有数据, 然后写入
# r 读取: 在读取文件数据的时候用到次模式
# wb 写入二进制数据(图片\视频\音频\字体文件)


# GBK  windows系统下默认的编码  gb2312 ...
with open('hello.txt', mode='a', encoding='utf-8') as f:
    f.write('你好\n')
