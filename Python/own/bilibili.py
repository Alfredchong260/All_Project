import json
import os
import ffmpeg
import requests
from lxml import etree
 
# 防止因https证书问题报错
requests.packages.urllib3.disable_warnings()

headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
 
    'Refer'
 
    'er': 'https://www.bilibili.com/'
}

'''
    获取bilibili视频的主要函数
    @param url 视频页面url 结构为:url?参数
    @param p 视频p数
    @param bv 视频bv数
'''

def main():
    # 输入bilibili视频的BV号
    bv = input('视频BV号：')

    url = 'https://www.bilibili.com/video/'+bv

# 选择视频从第几p开始到第几p结束

    startPart = input('起始P:')
    endPart = input('终止P;')

    for p in range(int(startPart),int(endPart) + 1):
        getBiliBiliVideo(url + '?p=' + str(p),p,bv)

def getBiliBiliVideo(url,p,bv):
 
    print("Starting requests")
    session = requests.session()
    res = session.get(url=url,headers=headers,verify=False)
    _element = etree.HTML(res.content)
 
    # 获取window.__playinfo__的json对象,[20:]表示截取'window.__playinfo__='后面的json字符串
    videoPlayInfo = str(_element.xpath('//head/script[5]/text()')[0].encode('utf-8').decode('utf-8'))[20:]
 
    videoJson = json.loads(videoPlayInfo)
 
    # 获取视频链接和音频链接
 
    print("BaseUrl")
    try:
        # 2018年以后的b站视频由.audio和.video组成
        videoURL = videoJson['data']['dash']['video'][0]['baseUrl']
        audioURl = videoJson['data']['dash']['audio'][0]['baseUrl']
        flag=0

    except Exception:
        # 2018年以前的b站视频音频视频结合在一起,后缀为.flv
        videoURL = videoJson['data']['durl'][0]['url']
        flag=1
 
    # 指定文件生成目录,如果不存在则创建目录
 
    dirname = ("blackpink/").encode("utf-8").decode("utf-8")
 
    if not os.path.exists(dirname):
        os.makedirs(dirname)
        print('文件夹创建成功!')
 
    print("Start to download video")
    # 获取每一集的名称
    name = bv + "-" + str(p)
 
    # 下载视频和音频
 
    print('正在下载 "'+name+'" 的视频····')
 
    print("File download function")
    fileDownload(homeurl=url,url=videoURL, name='blackpink/'+name + '_Video.mp4', session=session)
    print("Video Downloaded")
 
    if flag == 0:
 
        print('正在下载 "'+name+'" 的音频····')
 
        fileDownload(homeurl=url,url=audioURl, name='blackpink/'+name+ '_Audio.mp3', session=session)
        print("Audio Downloaded")
 
        print('正在组合 "'+name+'" 的视频和音频····')
 
        combineVideoAudio('blackpink/' + name + '_Video.mp4','blackpink/' + name + '_Audio.mp3','blackpink/' + name + '_output.mp4')
 
    print(' "'+name+'" 下载完成！')
 
 
'''
    使用session保持会话下载文件
    
    @param homeurl 访问来源
    
    @param url 音频或视频资源的链接
    
    @param name 下载后生成的文件名
    
    @session 用于保持会话
'''
 

def fileDownload(homeurl,url, name, session=requests.session()):
 
    # 添加请求头键值对,写上 refered:请求来源
 
    headers.update({'Referer': homeurl})
 
    # 发送option请求服务器分配资源
 
    session.options(url=url, headers=headers,verify=False)
 
    # 指定每次下载1M的数据
 
    begin = 0
 
    end = 1024*512 - 1
 
    flag = 0
 
    while True:
 
        # 添加请求头键值对,写上 range:请求字节范围
 
        headers.update({'Range': 'bytes=' + str(begin) + '-' + str(end)})
 
        # 获取视频分片
 
        res = session.get(url=url, headers=headers,verify=False)
 
        if res.status_code != 416:
 
            # 响应码不为为416时有数据
 
            begin = end + 1
 
            end = end + 1024*512
 
        else:
 
            headers.update({'Range': str(end + 1) + '-'})
 
            res = session.get(url=url, headers=headers,verify=False)
 
            flag=1
 
        with open(name.encode("utf-8").decode("utf-8"), 'ab') as fp:
 
            fp.write(res.content)
 
            fp.flush()
 
        # data=data+res.content
 
        if flag==1:
 
            fp.close()
 
            break
 
'''
    用于合并音频与视频
    @param videopath 视频路径
    @param audiopath 音频路径
    @param outpath 生成合并视频的路径
'''
 
def combineVideoAudio(videopath,audiopath,outpath):
 
    os.system(f'ffmpeg -i {videopath} -i {audiopath} -map 0:v -map 1:a -c:v copy -c:a copy {outpath} -y') 

    os.remove(videopath)
    os.remove(audiopath)
 
 
 
if __name__ == '__main__':
    main() 
