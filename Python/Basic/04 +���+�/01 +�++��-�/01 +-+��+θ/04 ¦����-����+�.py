import requests

img_data = requests.get('https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png').content


# 二进制数据没有编码
# wb 写入二进制数据的模式
with open('baidu.png', mode='wb') as f:
    f.write(img_data)

