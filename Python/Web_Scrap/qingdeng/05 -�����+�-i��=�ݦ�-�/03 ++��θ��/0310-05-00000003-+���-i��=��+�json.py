"""
1. 采集网址 https://haokan.baidu.com/tab/gaoxiao_new

2. 采集目标
	- 采集当前页面, "时下热门" 里面的数据
	- 需要需要采集以下数据:
		title 视频标题
		duration 视频时长
		comment  评论数量
		fmplaycnt 播放量

    - 用正则表达式采集
"""
from pprint import pprint
import requests
import json
import re

url = 'https://haokan.baidu.com/web/video/feed?tab=gaoxiao_new&act=pcFeed&pd=pc&num=5&shuaxin_id=1634613779446&hot=1'

headers = {
    'Cookie': 'BIDUPSID=C446A34D9A0E02D0A9DB1EF7C8F615B0; PSTM=1629201683; BAIDUID=68B47A0424275A7D6331D3654050A4AE:FG=1; BAIDUID_BFESS=9E3BDCB0DF63363F1046E90F96AFD8C2:FG=1; Hm_lvt_4aadd610dfd2f5972f1efee2653a2bc5=1634612861; Hm_lpvt_4aadd610dfd2f5972f1efee2653a2bc5=1634612861; ab_sr=1.0.1_Njc0NjkwOTZhMmY2MTU1Y2NiMzZlMTdjNDAzYTczODE5ZThkY2U0OTgxZjViNDczZjczYzM4MDUxNjEyNzRiMDk4OTNmZGQ2ZDViNDRhNTRmNGY2ODlhMTlkNzE3MDc1MTM2MzhiYWIwMjJlNjAwNDUwYTgyMWJmNmZmMzgzOGNkZjk2MWY3MzJiYjU3MjhhY2EwMDI5ODNiNjA5NzNjZA==; reptileData=%7B%22data%22%3A%22867137f256819a75e7f8c368cc8ec0892f41fe9d48895253c5b6b0783da541a07c693979bf81bc6bbd3425941c3cda80bda2408cb3482ebc74be27c10dbdfa18dc68a6ef6155b749366cb4ee1f70c8079b42e9ed621be0320981c8b4d49bbf3af60bb86a8f697d34c0386421cc927383d8defb6271fa1ac7efeea086bcdc9ef5%22%2C%22key_id%22%3A%2230%22%2C%22sign%22%3A%223b4ed137%22%7D',
    'Host': 'haokan.baidu.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

response = requests.get(url, headers=headers)
infos = json.dumps(response.json(), ensure_ascii=False)
title = re.findall('"title": "(.*?)"', infos, re.S)
duration = re.findall('"duration": "(.*?)"', infos, re.S)
comment = re.findall('"comment": "(\d+)"', infos, re.S)
fmplaycnt = re.findall('"fmplaycnt": "(.*?)"', infos, re.S)

for t, d, c, f in zip(title, duration, comment, fmplaycnt):
    print(f'标题：{t}\n时长：{d}\n评论：{c}\n播放量：{f}\n')
