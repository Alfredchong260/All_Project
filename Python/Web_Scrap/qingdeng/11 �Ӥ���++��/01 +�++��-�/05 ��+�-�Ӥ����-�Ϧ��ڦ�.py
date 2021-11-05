#
# import requests
# import re
# import time
#
#
# start_time = time.time()
# for page in range(1, 11):
#     print(f'==========正在爬取第{page}数据=========')
#     response = requests.get(f'https://fabiaoqing.com/biaoqing/lists/page/{page}.html')
#     html_data = response.text
#     # print(html_data)
#
#     # 解析数据
#     # <img class="ui image lazy" data-original="(.*?)" src=.*?
#     result = re.findall('<img class="ui image lazy" data-original="(.*?)" src=.*?', html_data, re.S)
#     # print(result)
#
#     for img_url in result:
#         response_2 = requests.get(img_url).content  # 得到的图片数据
#         file_name = img_url.split('/')[-1]
#
#         with open('img\\' + file_name, mode='wb') as f:
#             f.write(response_2)
#             print('下载完成:', file_name)


# print('执行时间:', time.time() - start_time)

"""
多任务实现必须借助函数
1. 找数据所对应的地址
2. 请求地址数据
3. 数据解析
4. 数据的保存
"""
import time

import requests
import re
import threading


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

    print('执行时间:', time.time() - start_time)

# 非常重要
# 主函数写好以后, 运行一下看看主函数运行有没有错误. 因为多任务的错误非常难以排查
# run('https://fabiaoqing.com/biaoqing/lists/page/')

# 无法控制线程数量  线程池
start_time = time.time()
for page in range(1, 11):
    url = f'https://fabiaoqing.com/biaoqing/lists/page/{page}.html'
    threading.Thread(target=run, args=(url,)).start()

"""
函数封装:
2. 请求地址数据
3. 数据解析
4. 数据的保存

主函数调度其他函数运行
"""
