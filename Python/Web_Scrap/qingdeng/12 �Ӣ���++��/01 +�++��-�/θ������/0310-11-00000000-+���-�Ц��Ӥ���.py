"""
	目标网址：https://www.duitang.com/
	
	作业描述：请在网页最上面搜索框输入关键字 “蜡笔小新” 进行搜索图片，根据搜索到的结果采集前十页图片
	
	作业要求：用多线程的方式实现
"""
import time

import requests
import concurrent.futures

"""
请求函数
解析函数
保存函数
"""


def send_requests(url):
    response = requests.get(url=url)
    return response  # 返回请求的响应体


def parse_data(data):
    data_list = data['data']['object_list']

    img_url_list = []  # 收集解析出来的每一个图片地址
    for data_ in data_list:
        img_url = data_['photo']['path']  # 图片地址
        img_url_list.append(img_url)

    return img_url_list


def save_data(file_name, data):
    with open('img\\' + file_name, mode='wb') as f:
        f.write(data)
        print('下载完成: ', file_name)


def run(url):
    json_data = send_requests(url).json()
    imgUrl_list = parse_data(json_data)  # 图片地址的列表

    for imgUrl in imgUrl_list:
        file_name = imgUrl.split('/')[-1]
        img_data = send_requests(imgUrl).content  # 获取请求图片的二进制数据
        save_data(file_name, img_data)


# 测试主函数是否能运行
# run('https://www.duitang.com/napi/blogv2/list/by_search/?kw=%E8%9C%A1%E7%AC%94%E5%B0%8F%E6%98%9F&after_id=24&type=feed&include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Clike_id%2Csender%2Calbum%2Creply_count%2Cfavorite_blog_id&_type=&_=1635940348724')


start_time = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
    # 线程池
    for page in range(10):  # 0123456789
        url = f'https://www.duitang.com/napi/blogv2/list/by_search/?kw=%E8%9C%A1%E7%AC%94%E5%B0%8F%E6%98%9F&after_id={page * 24}&type=feed&include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Clike_id%2Csender%2Calbum%2Creply_count%2Cfavorite_blog_id&_type=&_=1635940348724'
        executor.submit(run, url)

print('花费时间:', time.time() - start_time)
