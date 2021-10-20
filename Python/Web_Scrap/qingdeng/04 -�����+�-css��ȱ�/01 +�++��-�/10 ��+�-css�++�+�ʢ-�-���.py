"""
爬虫项目<案例>实现的步骤:
1. 找数据所对应的地址< url(统一资源定位符) >  系统分析网页性质 <静态数据/动态数据>
2. 请求地址数据(文本, js数据, 图片数据, css数据...)
3. 数据解析, 解析你想要的数据, 剔除不想要的数据(css选择器, xpath节点提取, 正则表达式)
4. 数据的保存 (本地文件<txt,Excel,json...>, 数据库)
"""

# 1. 找数据所对应的地址
import parsel
import requests

url = 'https://www.guahao.com/expert/all/%E5%85%A8%E5%9B%BD/all/%E4%B8%8D%E9%99%90'

# 2. 请求地址数据
response = requests.get(url=url)
html_data = response.text
# print(html_data)

# 3. 数据解析
# 3.1 转换数据类型
selector = parsel.Selector(html_data)
# 3.2 解析数据
lis = selector.css('.g-doctor-items.to-margin ul li')  # 所有li

for li in lis:
    doctor_name = li.css('.wrap>a::text').get()
    doctor_lever = li.css('dl dt::text').getall()[1].strip()
    doctor_kind = li.css('dd p:nth-child(1)::text').get()
    doctor_beloging = li.css('p:nth-child(2) .g-txt-ell::text').get()
    doctor_see_price = li.css('.infos.video span em:nth-child(2)::text').get().strip()

    """
    if doctor_see_price:
        doctor_see_price.strip()
    """

    print(doctor_name, doctor_lever, doctor_kind, doctor_beloging, doctor_see_price)
