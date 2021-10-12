"""
表情包爬取
将此页面下的前十页图片全部获取下来：https://fabiaoqing.com/biaoqing
"""
"""请下下方开始编写代码"""
import requests
import re

for page in range(1, 11):
    print(f'==========正在爬取第{page}数据=========')
    response = requests.get(f'https://fabiaoqing.com/biaoqing/lists/page/{page}.html')
    html_data = response.text
    # print(html_data)

    # 解析数据
    # <img class="ui image lazy" data-original="(.*?)" src=.*?
    result = re.findall('<img class="ui image lazy" data-original="(.*?)" src=.*?', html_data, re.S)
    # print(result)

    for img_url in result:
        response_2 = requests.get(img_url).content  # 得到的图片数据
        file_name = img_url.split('/')[-1]

        with open('img\\' + file_name, mode='wb') as f:
            f.write(response_2)
            print('下载完成:', file_name)
