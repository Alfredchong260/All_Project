import time
import requests
import concurrent.futures


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

def save_data(img_url):
    """根据传进来的一个图片地址, 请求以及保存数据"""
    img_data = send_requests(url=img_url).content
    file_name = img_url.split('/')[-1]
    with open('img\\' + file_name, mode='wb') as f:
        f.write(img_data)
        print('下载完成: ', file_name)

def run(url):
    json_data = send_requests(url).json()
    imgUrl_list = parse_data(json_data)  # 图片地址的列表

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as exe:
        # 线程池: 分发每一次请求图片地址的任务
        for imgUrl in imgUrl_list:  # 0123456789
            exe.submit(save_data, imgUrl)



if __name__ == '__main__':

    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=6) as executor:
        # 进程池:
        # 请求每一页 json 数据, 每一页json数据中心有若干个图片地址任务,
        # 任务分发给线程池执行
        for page in range(10):  # 0123456789
            url = f'https://www.duitang.com/napi/blogv2/list/by_search/?kw=%E8%9C%A1%E7%AC%94%E5%B0%8F%E6%98%9F&after_id={page * 24}&type=feed&include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Clike_id%2Csender%2Calbum%2Creply_count%2Cfavorite_blog_id&_type=&_=1635940348724'
            executor.submit(run, url)

    print('花费时间:', time.time() - start_time)

"""
多有的多任务都是基于函数对象的
如果我们多进程要嵌套多线程, 需要把多线程的逻辑放到一个函数对象里面(套娃)

只要不是操作的单个文件, 或者同一个全局变量, 那么数据就不会缺失
"""
