"""
    目标网址: https://nba.hupu.com/stats/players/pts
    
    需求:
        1、用xpath采集nba球员数据
        2、采集以下信息
            rank   # 排名
            player  # 球员
            team    # 球队
            score    # 得分
            hit_shot   # 命中-出手
            hit_rate   # 命中率
            hit_three   # 命中-三分
            three_rate   # 三分命中率
            hit_penalty   # 命中-罚球
            penalty_rate   # 罚球命中率
            session   # 场次
            playing_time   # 上场时间
            
        解析到数据用print()函数打印即可
请在下方编写代码：
"""

import requests
import parsel

url = 'https://nba.hupu.com/stats/players/pts'

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}

response = requests.get(url, headers=headers)
selector = parsel.Selector(response.text)

tr_list = selector.xpath("//table[@class='players_table']//tr")
head = tr_list[0].xpath('.//td/text()').getall()
for i in head:
    print(i, end='\t')

for tr in tr_list[1:]:
    rank = tr.xpath('./td[1]/text()').get()
    player = tr.xpath('./td[2]/a/text()').get()
    team = tr.xpath('./td[3]/a/text()').get()
    score = tr.xpath('./td[4]/text()').get()
    hit_shot = tr.xpath('./td[5]/text()').get()
    hit_rate = tr.xpath('./td[6]/text()').get()
    hit_three = tr.xpath('./td[7]/text()').get()
    three_rate = tr.xpath('./td[8]/text()').get()
    hit_penalty = tr.xpath('./td[9]/text()').get()
    penalty_rate = tr.xpath('./td[10]/text()').get()
    session = tr.xpath('./td[11]/text()').get()
    playing_time = tr.xpath('./td[12]/text()').get()
    print(f"{rank}\t{player}\t{team}\t{score}\t{hit_shot}\t{hit_rate}\t{hit_three}\t{three_rate}\t{hit_penalty}\t{penalty_rate}\t{session}\t{playing_time}")
