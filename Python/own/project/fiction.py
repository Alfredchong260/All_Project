'''
全局思路：
    得到需要的小说
    查询小说
    将小说的所有章节内容提取下来
    以tkinter建立gui页面让用户查看小说数据
        书名，作者，简介
    用户选择小说并开始下载小说内容
    将章节内容封装成txt文本

问题：
    有些小说是VIP的，不知怎么破解，暂且将这个项目放一放
'''

import requests
from lxml import etree
from tqdm import tqdm
import random
from tkinter import *
from tkinter import messagebox

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}

proxies = ['HTTP://110.243.30.23:9999', 'HTTP://222.189.191.206:9999',
            'HTTP://106.42.163.100:9999', 'HTTP://120.83.107.69:9999',
           'HTTP://60.13.42.135:9999',  'HTTP://113.195.232.23:9999',
           'HTTP://59.62.36.74:9000', 'HTTP://218.2.226.42:80']
proxy = {'HTTP': random.choice(proxies)}

class xiaoshuowang:
    def __init__(self, url):
        self.url = url 

    def main(self):
        response = requests.get(self.url, headers=headers, proxies=proxy)
        html = etree.HTML(response.text)
        page = html.xpath('//div[@class="pages"]/a[6]/text()')
        all_infos = self.getInfo(page)
        title = all_infos['title']
        artist = all_infos['artist']
        intro = all_infos['intro']
        with open('./data.txt', 'w') as w:
            for t, a, i in tqdm(zip(title, artist, intro)):
                    w.writelines([f"小说名：{t}\n{a}\n简介：{i}\n"])

        test = GUI()
        test.main()
        
    def getInfo(self, page):
        dic = {'title':[], 'artist':[], 'intro':[]}
        check = []

        try:
            for i in tqdm(range(int(page[0]) + 1)):
                response = requests.get(self.url + '&pageNo=' + str(i), headers=headers, proxies=proxy)
                html = etree.HTML(response.text)
                infos = html.xpath('//div[@class="info fl"]')

                for info in infos:
                    titles = info.xpath('./h3/a/@pbtag')
                    artists = info.xpath('div[1]/text()')
                    intros  = info.xpath('div[2]/text()')

                    for title, artist, intro in zip(titles, artists, intros):
                        if title not in check:
                            dic['title'].append(title.split('_')[-1])
                            dic['artist'].append(artist)
                            dic['intro'].append(''.join(intro).replace('\u3000', ''))
                            check.append(title)
            print('读取完成')

        except Exception:
            print('没有该名字的书籍')

        return dic

    def readData(self):
        titles = []
        artists = []
        intros = []
        with open('./data.txt', 'r') as r:
            for line in r:
                line = line.strip()
                if line.startswith('小说名：'):
                    title = line.split('小说名：')[1]
                    titles.append(title)
                elif line.startswith('作者：'):
                    artist = line.split('作者：')[1]
                    artists.append(artist)
                elif line.startswith('简介：'):
                    intro = line.split('简介：')[1]
                    intros.append(intro)

        return [titles, artists, intros]

    def downloadFiction(self):
        pass

class GUI:
    def main(self):
        root = Tk()
        root.title('小说下载器')
        root.geometry('800x800+250+250')
        root.configure(bg='sky blue')

        frame = Frame(root, width=600)
        frame.grid(column=0, row=0, padx=10, pady=10)

        scrollbar = Scrollbar(frame, bg='light gray')
        scrollbar.pack(side=RIGHT, fill=Y)
        global l
        l = Listbox(frame, yscrollcommand=scrollbar.set, font=('', 20), width=40, height=30)
        l.pack(side=LEFT)
        scrollbar.config(command=l.yview)

        test = xiaoshuowang(url)
        data = test.readData()
        for i in data[0]:
            l.insert(END, i)
        
        button = Button(root, text='查看', padx=20, pady=15, font=('', 18), command=self.lookup)
        button.grid(row=1, column=0)

        root.mainloop()

    def lookup(self):
        top = Toplevel(bg='sky blue')
        value = l.curselection()

        frame = Frame(top, width=600)
        frame.grid(column=0, row=0, padx=10, pady=10)

        scroll = Scrollbar(frame, bg='light gray', orient=HORIZONTAL)
        scroll.pack(side=BOTTOM, fill=X)
        list = Listbox(frame, xscrollcommand=scroll.set, font=('', 20), width=60, height=20)
        list.pack(side=LEFT)
        scroll.config(command=list.xview)
        if value:
            index = value[0]
            val = l.get(index)

            test = xiaoshuowang(url)
            data = test.readData()
            titles = data[0]
            artists = data[1]
            intros = data[2]
            for title in titles:
                index = titles.index(title)
                if title == val:
                    list.insert(END, f"书名：{titles[index]}")
                    list.insert(END, f"作者：{artists[index]}")
                    intro = intros[index].split('，')
                    list.insert(END, f"简介：{intro[0]}")
                    for i in intro[1::]:
                        list.insert(END, f"            {i},\n")

        confirm_btn = Button(top, text='确认', command=lambda: self.confirm(top)).grid(row=1, column=1)

    def confirm(self, top):
        response = messagebox.askokcancel('二次确认','是否确定要下载此小说')

        if response:
            test = xiaoshuowang(url)
            top.destroy()

if __name__ == "__main__":
    word = input('请输入您要查找的小说名：')
    global url
    url = f'https://xs.sogou.com/0_0_0_0_heat/?keyword={word}'
    test = GUI()
    # test = xiaoshuowang(url)
    test.main()
