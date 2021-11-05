import time

import requests
import re
import concurrent.futures

def send_requests(url):
    """发送请求的函数"""
    response = requests.get(url=url)
    return response

def parse_data(html):
    """数据解析函数, 传入数据进行解析"""
    result_list = re.findall('<img class="ui image lazy" data-original="(.*?)" src=.*?', html, re.S)
    return result_list  # 返回图片地址  --- 列表

def save_data(file_name, data):
    """
    保存数据的方法
    :param file_name: 文件名字
    :param data: 数据
    """
    with open('img\\' + file_name, mode='wb') as f:
        f.write(data)
        print('保存完成:', file_name)



# 转换函数对象，只针对一个函数任务才能转换
# 可以定义一个主函数，去吧其他函数任务的逻辑在主函数实现
def run(url):
    """主函数, 调用其他函数任务执行"""
    # 1. 调用发送网络请求的方法
    html_data = send_requests(url).text
    # 2. 调用数据解析的方法, 得到图片地址列表
    img_Url_list = parse_data(html_data)

    for img_Url in img_Url_list:  # 遍历图片地址
        img_data = send_requests(img_Url).content  # 请求的图片数据
        file_name = img_Url.split('/')[-1]  # 文件名
        # 3. 调用数据保存的方法
        save_data(file_name, img_data)

    # print('执行时间:', time.time() - start_time)

# start_time = time.time()
# for page in range(1, 11):
#     url = f'https://fabiaoqing.com/biaoqing/lists/page/{page}.html'
#     threading.Thread(target=run, args=(url,)).start()


start_time = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    for page in range(1, 11):
        url = f'https://fabiaoqing.com/biaoqing/lists/page/{page}.html'
        executor.submit(run, url)
print('执行时间:', time.time() - start_time)

"""
线程池可以控制任务执行的数量
用的多的
"""
