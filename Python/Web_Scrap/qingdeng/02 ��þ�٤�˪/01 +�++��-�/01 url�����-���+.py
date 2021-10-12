
import requests


response = requests.get(f'https://www.hexuexiao.cn/a/124525-0.html')
"""
https://www.baidu.hexuexiao.cn.com/a/124525-0.html

https://        请求协议的类型(http/https), 超文本传输协议(文字, 网页数据, 图片, 音频, 视频...)
www             服务器名字  www (world wide web) 万维网, mail(邮件服务器名字)
hexuexiao.cn    表示域名(scrapy爬虫框架)
/               服务器的根目录(树形结构)
a/124525-0.html 资源位置, 类似于电脑的盘符

https://www.baidu.hexuexiao.cn.com/a/124525-0.html
    链接地址
    url
    ip地址
    接口
"""