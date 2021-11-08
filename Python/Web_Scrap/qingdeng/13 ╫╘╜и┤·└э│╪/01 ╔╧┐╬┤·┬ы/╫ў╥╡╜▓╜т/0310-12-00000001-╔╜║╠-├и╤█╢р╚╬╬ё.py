"""
	目标网址: https://maoyan.com/board/4?offset=0
	
    猫眼100网页, 请用多进程嵌套多线程池方式实现

温馨提示: 猫眼封ip严重, 在确保代码无误的情况下尽量少运行。考验代码能力的时候来了。。。
请在下方编写代码

"""
import csv

import requests
import parsel
import concurrent.futures
import threading


lock = threading.Lock()

headers = {
    'Cookie': '__mta=244152890.1603971211691.1618042413519.1618044198851.63; __mta=244152890.1603971211691.1618044198851.1634737108531.64; __mta=244152890.1603971211691.1618044198851.1636113350065.64; _lxsdk_cuid=1757422618bc8-00cec1fb04d25d-303464-1fa400-1757422618bc8; __mta=244152890.1603971211691.1632809679672.1632897727972.102; uuid_n_v=v1; uuid=2CA15B803E2F11EC89993550E45107B0ACB2725E5F644BB6BBA200295D260EFD; _csrf=b08b0e45a1ab295ee99c41d16dc4bfd3a5c9b9802c8523fb37269f7c0f3aadfe; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1634302984,1634556705,1634733558,1636113288; _lxsdk=2CA15B803E2F11EC89993550E45107B0ACB2725E5F644BB6BBA200295D260EFD; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1636113350; _lxsdk_s=17ceff38a92-bd9-93f-8ea%7C%7C14',
    'Host': 'www.maoyan.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
}


def send_requests(url):
    """发送请求的函数"""
    response = requests.get(url=url, headers=headers)
    return response.text


def parse_data(data):
    selector = parsel.Selector(data)
    dds = selector.css('.board-wrapper>dd')  # 所有的dd标签

    data_list = []  # 数据的二维列表
    for dd in dds:
        name = dd.css('.name a::text').get()
        star = dd.css('.star::text').get().strip()
        releasetime = dd.css('.releasetime::text').get().strip()
        score = dd.css('.score i::text').getall()
        score = ''.join(score)
        print(name, star, releasetime, score)
        data_list.append([name, star, releasetime, score])
    return data_list


def save_data(data_):  # 保存函数, 只保存一条数据

    with open('猫眼.csv', mode='a', encoding='utf-8', newline='') as f:
        csv_write = csv.writer(f)
        lock.acquire()
        csv_write.writerow(data_)
        lock.release()


def run(url):
    html_data =send_requests(url)
    data_list = parse_data(html_data)  # 二维列表

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as exe:  # 用多线程进行每一条数据保存
        for data in data_list:
            exe.submit(save_data, data)


# run('https://www.maoyan.com/board/4?offset=0')

if __name__ == '__main__':

    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        for page in range(0, 91, 10):
            url = f'https://www.maoyan.com/board/4?offset={page}'
            executor.submit(run, url)

