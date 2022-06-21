import requests
import os

base_dir = '/home/cms/.Project/Python/own/scrap/'

# base url
url = "https://v2.kwaicdn.com/upic/2022/06/09/21/BMjAyMjA2MDkyMTI0MzJfOTIwODI2MF83NjQwNzE2NzE2M18xXzM=_hd15_Bda4b14c46f7159110255b35606bcf44f.mp4?pkey=AAXqvdLlBGN2-9rjbfW9KbH7QLApBs65ehKCAzlIxJkLdDwoS_kBgSBOqIaUuE-PxMWSz-BYY8Kfvdj2oYsnFD70sFmYRQmU4z3Z67zUX3ZJjfFjY0E1WJGam9iMLfo5sXo&tag=1-1655193519-unknown-0-ipped5taht-b4d1d543acbfc432&clientCacheKey=3xd4g6kc4g4qqcw_hd15.mp4&di=b44bf327&bp=10004&tt=hd15&ss=vp"

# get the response
response = requests.get(url)

print('download completed')
with open(base_dir + '帐号已注销.mp4', 'wb')as fs:
    fs.write(response.content)


# build the command that we want  to run
cmd = f"ffmpeg -i {base_dir + '帐号已注销.mp4'} -vn {base_dir + '帐号已注销.mp3'}"
cmd2 = f'rm -rf {base_dir + "帐号已注销.mp4"}'
os.system(cmd)
os.system(cmd2)
print('convertion completed')

