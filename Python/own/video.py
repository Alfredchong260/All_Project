import requests
import re
import tkinter

headers = {
 
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3970.5 Safari/537.36',
 
    'Refer'
 
    'er': 'https://www.bilibili.com/'
 
}
r = requests.get('https://v.cnv3.com/', headers=headers)
# print(r.text)
rg = re.compile('value="(.*?)"')
rs = re.findall(rg, r.text)
print(rs)
dk_one = 'https:' + rs[0]
dk_two = 'https:' + rs[1]
dk_three = 'https:' + rs[2]
dk_four = 'https:' + rs[3]

root = tkinter.Tk()
root.geometry('413x150')
root.mainloop()
