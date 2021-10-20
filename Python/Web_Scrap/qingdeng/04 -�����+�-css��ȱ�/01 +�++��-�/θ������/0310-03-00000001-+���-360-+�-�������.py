"""
	- 课上的360案例，先自己实现一遍, 构建查询参数请求数据
	- 将前三页的图片数据保存下来
		
请在下方编写代码
"""

import requests
import pprint


# 1.找数据地址
url = 'https://image.so.com/j'

def get_params(page):
    """构建查询参数"""

    params = {
        'q': '风景',
        'pd': '1',
        'pn': '60',
        'correct': '风景',
        'adstar': '0',
        'tab': 'all',
        'sid': 'c18fe3dff9a3d8d70eeee7e8952cdbbf',
        'ras': '0',
        'cn': '0',
        'gn': '0',
        'kn': '0',
        'crn': '0',
        'bxn': '0',
        'cuben': '0',
        'pornn': '0',
        'manun': '0',
        'src': 'srp',
        'color': 'yellow',
        'sn': page,
        'ps': page,
        'pc': '60',
    }
    return params

# 2.发送请求

count = 0  # 记录图片数量
for i in range(60, 181, 60):
    params = get_params(i)
    response = requests.get(url=url, params=params)
    json_data = response.json()
    # pprint.pprint(json_data)

    # 3.数据解析
    list_data = json_data['list']
    for data in list_data:
        img_url = data['img']
        print(img_url)

        # 保存图片
        # 1. 请求图片数据
        try:
            img_data = requests.get(url=img_url, timeout=3).content
        except Exception as e:
            print(e)
            continue
        # 2. 保存的文件名
        file_name = str(count) + '.jpg'
        with open('img\\' + file_name, mode='wb') as f:
            f.write(img_data)
            print('保存完成:', file_name)

        count += 1


    print('*' * 100)




