import requests
import re
import os
from lxml import etree
from tqdm import tqdm
from tkinter import *
from tkinter import messagebox

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0'
}

filename = './img/'

if not os.path.exists(filename):
    os.mkdir(filename)

class imageDownloader:

    def main(self, tag, num):
        print('开始准备工作')
        print('开始运作程序')
        for page in tqdm(range(1, num + 1)):
            url = f'https://m.bcoderss.com/tag/{tag}/page/{page}/'
            self.getInfo(url)

    def getInfo(self, url):
        response = requests.get(url, headers=headers)
        html = etree.HTML(response.text)
        infos = html.xpath('//ul[@class="wallpaper"]/li')
        urls = []
        for info in infos:
            link = info.xpath('./a/img/@src')
            for i in link:
                if '-260x534' in i:
                    a = i.split('-260x534')
                    url = a[0] + a[1]
                    urls.append(url)

                else:
                    urls.append(i)

        for url in urls:
            title = re.findall('https://.*/.*/uploads/\d+/\d\d/(.*)', url)
            self.download(url, title[0])


    def download(self, link, title):
        img_content = requests.get(url=link, headers=headers)
        with open(filename + title, 'wb+') as w:
            w.write(img_content.content)

    def getTitle(self, url):
        response = requests.get(url, headers=headers)
        name = re.findall('<li><a href=".*?" class=".*?" style=".*?">(.*?)</a></li>', response.text)

        return name

class GUI:
    def main(self):
        global root
        root = Tk()
        root.geometry('500x500+500+300')
        root.configure(bg='light gray')
        # root.overrideredirect(True)
        root.minimized = False
        root.maximized = False

        self.titleBar()
        self.innerPart()

        root.mainloop()

    def titleBar(self):
        def minimize_me():
            root.attributes("-alpha",0) # so you can't see the window when is minimized
            root.minimized = True       

        def maximize_me():
            if root.maximized == False: # if the window was not maximized
                root.normal_size = root.geometry()
                expand_btn.config(text=" 🗗 ")
                root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
                root.maximized = not root.maximized 
                # now it's maximized
                
            else: # if the window was maximized
                expand_btn.config(text=" 🗖 ")
                root.geometry(root.normal_size)
                root.maximized = not root.maximized

        global scrollbar
        scrollbar = Scrollbar(root)
        scrollbar.pack(side=RIGHT, fill=Y)

        title_bar = Frame(root, bg='#2e2e2e', relief='raised', bd=0, highlightthickness=0)
        title_bar.pack(side=TOP, fill=X)

        title = Label(title_bar, text='选择器', bg='#2e2e2e', fg='white', bd=0, font=('', 15))
        title.pack(side=LEFT, padx=10)

        close_btn = Button(title_bar, text=' X ', bg='#2e2e2e', padx=2, pady=2,\
            fg='white', font=('', 15), command=root.destroy)
        close_btn.pack(side=RIGHT, ipadx=7, ipady=1)

        expand_btn = Button(title_bar, text=' 🗖 ', bg='#2e2e2e', padx=2, pady=2, fg='white',\
            bd=2, font=('', 15), command=maximize_me)
        expand_btn.pack(side=RIGHT, ipadx=7, ipady=1)

        min_btn = Button(title_bar, text='  -  ', bg='#2e2e2e', padx=2, pady=2, fg='white',\
            bd=2, font=('', 15), command=minimize_me)
        min_btn.pack(side=RIGHT, ipadx=1, ipady=1)
            
        title_bar.bind('<B1-Motion>', self.move)
        title.bind('<B1-Motion>', self.move)

    def move(self, event):
        root.geometry(f'+{event.x_root}+{event.y_root}')

    def innerPart(self):
        global l
        l = Listbox(root, yscrollcommand=scrollbar.set, font=('', 20), width=15, height=10)
        l.pack(side=LEFT)
        scrollbar.config(command=l.yview)

        url = 'https://m.bcoderss.com/'
        test = imageDownloader()
        names = test.getTitle(url)

        self.bttn('确认', '#ffcc66', '#141414', lambda:self.func())
        for name in names:
            l.insert(END, name)

        title = Label(root, text='请输入你要爬取的页面数量', font=('', 15), padx=10, pady=10)
        title.pack()

        global entry
        entry = Entry(root, font=('', 15))
        entry.pack(side=LEFT)

    def bttn(self, text, bcolor, fcolor, cmd):

        def on_enter(e):
            myButton['background']=bcolor
            myButton['foreground']=fcolor

        def on_leave(e):
            myButton['background']=fcolor
            myButton['foreground']=bcolor

        myButton = Button(root, width=30, height=2, text=text,
                          font=('', 15),
                          fg=bcolor,
                          bg=fcolor,
                          border=0,
                          activeforeground=fcolor,
                          activebackground=bcolor,
                          command=cmd,)

        myButton.bind('<Enter>', on_enter)
        myButton.bind('<Leave>', on_leave)

        myButton.pack(side=BOTTOM)

    def func(self):
        ask = messagebox.askokcancel('二次确认', '是否以这个标签对该网页进行访问')

        if ask:
            data = ''
            for i in l.curselection():
                data += l.get(i)
            try:
                page = int(entry.get())
                entry.delete(0, END)

            except:
                entry.delete(0, END)
                messagebox.askretrycancel('只允许数字，请重试', '只允许数字，请重试')

            download = imageDownloader()
            download.main(tag=data, num=page)


if __name__ == '__main__':
    test = GUI()
    test.main()
