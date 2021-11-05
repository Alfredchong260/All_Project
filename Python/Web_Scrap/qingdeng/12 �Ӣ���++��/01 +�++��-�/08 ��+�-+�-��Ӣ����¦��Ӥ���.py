import time
import requests
import concurrent.futures

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}


def send_requests(url):
    response = requests.get(url=url, headers=headers)
    return response  # 返回请求的响应体


def parse_data(data):
    data_list = data['data']
    video_list = []  # 收集解析出来的每一个视频数据

    for data_ in data_list:
        video_name = data_['title']  # 视频标题
        video_url = data_['playUrl']  # 视频url地址
        video_list.append([video_name, video_url])

    return video_list


def save_data(video_data):  # video_list 解析的当前请求的所有视频数据  [video_name, video_url]
    """根据传进来的一个图片地址, 请求以及保存数据"""
    mp4_data = send_requests(url=video_data[1]).content

    file_name = video_data[0]
    with open('video\\' + file_name + '.mp4', mode='wb') as f:
        f.write(mp4_data)
        print('下载完成: ', file_name)


def run(url):
    json_data = send_requests(url).json()
    video_list = parse_data(json_data)  # 视频地址的列表

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as exe:
        # 线程池: 分发每一次请求图片地址的任务
        for video in video_list:  # [[video_name, video_url],[], [], ...]
            exe.submit(save_data, video)


if __name__ == '__main__':

    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=6) as executor:
        # 进程池:
        # 请求每一页 json 数据, 每一页json数据中心有若干个图片地址任务,
        # 任务分发给线程池执行
        for page in range(5):  # 0123456789
            url = f'https://www.ku6.com/video/feed?pageNo={page}&pageSize=40&subjectId=76'
            executor.submit(run, url)

    print('花费时间:', time.time() - start_time)

