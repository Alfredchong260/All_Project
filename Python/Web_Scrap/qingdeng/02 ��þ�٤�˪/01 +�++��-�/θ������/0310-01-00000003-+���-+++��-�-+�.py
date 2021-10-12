"""
上课爬取图片的案例

	课上讲解是的爬取 香气四溢的薯条 (1/10) 这个系列图片,
	这个系列一共十张, 要求大家一次性将一个系列图片全部爬取下来

	地址： https://www.hexuexiao.cn/a/124525.html

请下下方开始编写代码
"""
# https://www.hexuexiao.cn/a/124525.html
import requests
import re


for page in range(10):
    response = requests.get(f'https://www.hexuexiao.cn/a/124525-{page}.html')

    html_data = response.text
    # print(html_data)


    """
    <a class="btn btn-default btn-xs" href="(.*?)" role="button" target="_blank">
    """
    result = re.findall('<a class="btn btn-default btn-xs" href="(.*?)" role="button" target="_blank">', html_data, re.S)
    print(result)

    # 图片地址
    img_url = result[0]

    # 请求图片地址
    # 图片\视频\音频\字体文件   都是二进制数据
    response_2 = requests.get(img_url)

    # content 从对象提取二进制数据
    img_data = response_2.content

    # 文件名
    file_name = img_url.split('/')[-1]
    print(file_name)

    # 保存文件
    with open(file_name, mode='wb') as f:
        f.write(img_data)



