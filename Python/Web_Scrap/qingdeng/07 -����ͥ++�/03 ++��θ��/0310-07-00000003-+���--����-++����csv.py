"""
目标站点:https://news.163.com/

往下翻有 要闻 这个新闻类目

    需求:
        爬取网易新闻 要闻 类目第一页数据，将数据保存为csv格式
        保存字段需要以下内容

            title  
            channelname  
            docurl  
            imgurl  
            source  
            tlink
"""
from tqdm import tqdm
import requests
import csv
import re

url = 'https://news.163.com/special/cm_yaowen20200213/?callback=data_callback'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}

response = requests.get(url)

title = re.findall('"title":"(.*?)",', response.text, re.S)
channelname = re.findall('"channelname":"(.*?)",', response.text, re.S)
docurl = re.findall('"docurl":"(.*?)",', response.text, re.S)
imgurl = re.findall('"imgurl":"(.*?)",', response.text, re.S)
source = re.findall('"source":"(.*?)",', response.text, re.S)
tlink = re.findall('tlink":"(.*?)",', response.text, re.S)

with open('网易新闻.csv', 'w', encoding='utf-8') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['title', 'channelname', 'docurl', 'imgurl', 'source', 'tlink'])
    for t, c, d, i, s, tl in tqdm(zip(title, channelname, docurl, imgurl, source, tlink), desc='正在写入数据'):
        information = [t, c, d, i, s, tl]
        csv_writer.writerow(information)
