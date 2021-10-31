from pprint import pprint
from tqdm import tqdm
import requests
import time
import json

url = 'https://student-api.iyincaishijiao.com/ep/course/lessons/?course_id=6973475615131310373&count=20&cursor=0&direction=1&course_version=1.1&anchor_type=1&api_version=2.0&device_id=1634370905119443&iid=&version_code=&channel=release&device_type=&aid=4783&app_name=ep_pc&device_platform=pc&app_id=4783&course_type=2&goods_id=6973475615131310373'

headers = {
    'cookie': '_tea_utm_cache_4783=undefined; MONITOR_WEB_ID=75352392-f128-4e36-a9e9-1978c80d68c4; s_v_web_id=verify_kutibk9j_mUPriAlv_s2ob_448R_8rtj_Asrt2qYZpDUE; passport_csrf_token_default=f2ccf493e3547ca13478de61574d6392; n_mh=B0nx9dwVZ4Ucd-8Xoh6UNSDbBCbYBwMu45mZKIOSNMw; passport_auth_status=beaa6e3a8d2f1de73b6fa049ebeb62bc%2C; passport_auth_status_ss=beaa6e3a8d2f1de73b6fa049ebeb62bc%2C; sid_guard=8c540af8215e7ac7cbbc956a708d2aa5%7C1634371043%7C5184000%7CWed%2C+15-Dec-2021+07%3A57%3A23+GMT; uid_tt=726b4cd468a832fda98a93b25082393f; uid_tt_ss=726b4cd468a832fda98a93b25082393f; sid_tt=8c540af8215e7ac7cbbc956a708d2aa5; sessionid=8c540af8215e7ac7cbbc956a708d2aa5; sessionid_ss=8c540af8215e7ac7cbbc956a708d2aa5; sid_ucp_v1=1.0.0-KGQwMzYyYmE2NzQwODY3MWFiOGIzOWU4YjczODVkYjdkM2M3Mjk3YmUKFgiH1MD_u4yuBBDji6qLBhivJTgIQCYaAmxmIiA4YzU0MGFmODIxNWU3YWM3Y2JiYzk1NmE3MDhkMmFhNQ; ssid_ucp_v1=1.0.0-KGQwMzYyYmE2NzQwODY3MWFiOGIzOWU4YjczODVkYjdkM2M3Mjk3YmUKFgiH1MD_u4yuBBDji6qLBhivJTgIQCYaAmxmIiA4YzU0MGFmODIxNWU3YWM3Y2JiYzk1NmE3MDhkMmFhNQ; passport_csrf_token=f2ccf493e3547ca13478de61574d6392; gftoken=OGM1NDBhZjgyMXwxNjM0MzcxMDQ3Mzl8fDAGBgYGBgY',
    'referer': 'https://student-api.iyincaishijiao.com/ep/pc/course-detail?course_type=2&goods_id=6973475615131310373',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}


header = {
    'origin': 'https://student-api.iyincaishijiao.com',
    'referer': 'https://student-api.iyincaishijiao.com/',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

response = requests.get(url=url, headers=headers)
infos = response.json()['data']['data']

ids = []

for info in tqdm(infos):
    data = json.loads((info['lesson_info']['video']['video_model']))
    ids.append(data['video_id'])

response.close()


m3u8 = []

# for id in ids:
#     MAIN = f'https://vod.bytedanceapi.com/?Action=GetPlayInfo&Version=2019-03-15&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKLTMGUzZDliMWZkOGM4NDJhMGI5MzA5MTBhNWI0ZDZiMTg%2F20211016%2Fcn-north-1%2Fvod%2Faws4_request&X-Amz-Date=20211016T135015Z&X-Amz-Expires=7200&X-Amz-NotSignBody=&X-Amz-Signature=66613d87cb44c3cb0254b45e25cac48e1b923039f7cd175bee9509d34e920540&X-Amz-SignedHeaders=&X-Amz-SignedQueries=Action%3BVersion%3BX-Amz-Algorithm%3BX-Amz-Credential%3BX-Amz-Date%3BX-Amz-Expires%3BX-Amz-NotSignBody%3BX-Amz-SignedHeaders%3BX-Amz-SignedQueries%3Bcodec_type%3Bdefinition%3Bformat_type%3Bstream_type%3Bvideo_id&codec_type=0&definition=0&format_type=hls&stream_type=evideo&video_id={id}&ssl=true'

#     main = 'https://vod.bytedanceapi.com/?Action=GetPlayInfo&Version=2019-03-15&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKLTMGUzZDliMWZkOGM4NDJhMGI5MzA5MTBhNWI0ZDZiMTg%2F20211016%2Fcn-north-1%2Fvod%2Faws4_request&X-Amz-Date=20211016T135857Z&X-Amz-Expires=7200&X-Amz-NotSignBody=&X-Amz-Signature=893bae384d4e52a3e319810d00a92be3b440c5a18d9fdd48685d4e021c775459&X-Amz-SignedHeaders=&X-Amz-SignedQueries=Action%3BVersion%3BX-Amz-Algorithm%3BX-Amz-Credential%3BX-Amz-Date%3BX-Amz-Expires%3BX-Amz-NotSignBody%3BX-Amz-SignedHeaders%3BX-Amz-SignedQueries%3Bcodec_type%3Bdefinition%3Bformat_type%3Bstream_type%3Bvideo_id&codec_type=0&definition=0&format_type=hls&stream_type=evideo&video_id=v02b01g10000c33c6ghkcb8ot59k3jf0&ssl=true'
    

#     print(id)
#     time.sleep(1)
#     response1 = requests.get(url=MAIN, headers=header)
#     json_data = response1.json()
#     data = json_data['Result']['Data']['PlayInfoList'][0]['BackupPlayUrl']
#     print(data)
#     time.sleep(1)

# print(m3u8)

key_url = 'https://kds.bytedance.com/kds/api/v1/keys?source=jarvis&ak=61163bb56c39fcee593a81860102b01b&token=HMAC-SHA1%3A1.0%3A1634392317%3AAKLTMGUzZDliMWZkOGM4NDJhMGI5MzA5MTBhNWI0ZDZiMTg%3ALcP6Vn5rffZ2OlH3uAZa3Dod5IY%3D'

head = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

response2 = requests.get(key_url, headers=head)
print(response2.json())
