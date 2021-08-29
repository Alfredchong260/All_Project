'''
全局思路：
    得到需要的东西
    把数据进行整合
    将数据写入txt文件
'''
import requests 

url = 'https://api.iyk0.com/xjj'
response = requests.get(url)
# binary
with open('xjj.jpg', 'wb') as w:
    w.write(response.content)
