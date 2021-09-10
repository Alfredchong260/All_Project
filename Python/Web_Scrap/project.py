import requests
import os

def getTsUrl():
    ts_url_list = []
    baseUrl = "https://ycalvod.yicai.com/record/live"
    with open("ca233887-1443-4bdf-b762-3b4b3a217085_LD.m3u8", "r", encoding="utf-8") as f:
        m3u8Contents = f.readlines()
        for content in m3u8Contents:
            if content.endswith("ts\n"):
                ts_Url = baseUrl + content.replace("\n", "").replace("..", "")
                ts_url_list.append(ts_Url)
                print(ts_Url)
    return ts_url_list

def download_ts_video(download_path, ts_url_list):
    download_path = r"C:\Users\Administrator\Desktop\AiShu\下载视频\TS视频"
    for i in range(len(ts_url_list)):
        ts_url = ts_url_list[i]
        try:
            response = requests.get(ts_url, stream=True, verify=False)
        except Exception as e:
            print("异常请求：%s" % e.args)
            return
        ts_path = download_path + "\{}.ts".format(i)
        with open(ts_path, "wb+") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
    print("TS文件下载完毕！！")

def heBingTsVideo(download_path,hebing_path):
    all_ts = os.listdir(download_path)
    with open(hebing_path, 'wb+') as f:
        for i in range(len(all_ts)):
            ts_video_path = os.path.join(download_path, all_ts[i])
            f.write(open(ts_video_path, 'rb').read())
    print("合并完成！！")

if __name__ == '__main__':
    download_path = r"C:\Users\Administrator\Desktop\AiShu\下载视频\TS视频"
    hebing_path = r"C:\Users\Administrator\Desktop\AiShu\下载视频\合并TS视频\第一财经.mp4"
    ts_url_list = getTsUrl()
    download_ts_video(download_path, ts_url_list)
    heBingTsVideo(download_path,hebing_path)
