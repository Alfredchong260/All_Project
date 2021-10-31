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

import requests
import re

url = 'https://haokan.baidu.com/web/video/feed?tab=gaoxiao_new&act=pcFeed&pd=pc&num=5&shuaxin_id=1634731283602&hot=1'

response = requests.get(url=url)
json_data = response.json()  # 字典  # 用text属性提取json数据会返回 Unicode 编码数据
print(json_data)

"""
{'id': '6785426150270266169', 'title': '姑娘和小伙相亲，没想俩人的名字一个比一个逗，人才啊', 'poster_small': 'https://f7.baidu.com/it/u=2245861802,2254874745&fm=222&app=108&f=JPEG@s_0,w_660,h_370,q_80', 'poster_big': 'https://f7.baidu.com/it/u=2245861802,2254874745&fm=222&app=108&f=JPEG@s_0,w_660,h_370,q_80', 'poster_pc': 'https://f7.baidu.com/it/u=2245861802,2254874745&fm=222&app=108&f=JPEG@s_0,w_660,h_370,q_80', 'source_name': '墙人搞笑', 'play_url': 'http://vd2.bdstatic.com/mda-mgsdshn7viyqm1dk/cae_h264_nowatermark/1627379762609313819/mda-mgsdshn7viyqm1dk.mp4?v_from_s=hkapp-haokan-nanjing', 'duration': '02:54', 'url': 'https://haokan.hao123.com/v?vid=6785426150270266169&pd=pc&context=', 'show_tag': 0, 'publish_time': '2021年07月27日', 'is_pay_column': 0, 'like': '7666', 'comment': '89', 'playcnt': '1253430', 'fmplaycnt': '125万次播放', 'fmplaycnt_2': '125万', 'outstand_tag': '', 'previewUrlHttp': 'https://vd2.bdstatic.com/mda-mgsdshn7viyqm1dk/cae_h264_nowatermark/1627379762609313819/mda-mgsdshn7viyqm1dk.mp4?v_from_s=hkapp-haokan-nanjing&auth_key=1634733485-0-0-f7ac588e840670ac6750fe6b8ce81eca&bcevod_channel=searchbox_feed&pd=1&vt=1&cd=0&watermark=0&did=&logid=0485220110&vid=6785426150270266169&pt=0&appver=&model=&cr=0&abtest=peav_l52&sle=1&sl=660&split=619640'}
{.*?'title': '(.*?)',.*?, 'duration': '(.*?)',.*?'comment': '(.*?)',.*?'fmplaycnt': '(,*?)',.*?}
\{.*?'title': '(.*?)',.*?, 'duration': '(.*?)',.*?'comment': '(.*?)',.*?'fmplaycnt': '(,*?)',.*?\}
"""
result = re.findall(
    "\{.*?'title': '(.*?)',.*?, 'duration': '(.*?)',.*?'comment': '(.*?)',.*?'fmplaycnt': '(.*?)',.*?\}",
    str(json_data), re.S)
print(result)
