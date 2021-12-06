"""
    图片已经加载好了，请参考 `图片查看器.png` 实现图片查看器的逻辑
"""

import tkinter as tk
import glob

from PIL import Image, ImageTk


"""在下面实现代码"""
class ImgViewer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('图片查看器')
        # 加载本地图片
        self.photos = glob.glob('photo/*.jpg')
        self.photos = [ImageTk.PhotoImage(
            Image.open(file)) for file in self.photos]

        self.img_frame = tk.Frame(self.root)
        self.img_frame.pack()
        self.label_frame = tk.Frame(self.root)
        self.label_frame.pack()

        self.page = 0

        self.create_page()
        self.root.mainloop()

    def next_page(self):
        self.page += 1

        self.btn_previous = tk.Button(self.label_frame, text='上一页',
                                      command=self.pre_page).grid(row=2, column=1)
        self.label_img.config(image=self.photos[self.page])
        self.check()
        self.page_label.config(text=f'{self.page + 1} of {len(self.photos)}')

        if self.page + 1 == len(self.photos):
            self.btn_next = tk.Button(self.label_frame, text='下一页',
                                      command=self.next_page, state=tk.DISABLED).grid(row=2, column=2)

    def pre_page(self):
        self.page -= 1
        self.btn_next = tk.Button(self.label_frame, text='下一页',
                                  command=self.next_page).grid(row=2, column=2)
        self.label_img.config(image=self.photos[self.page])
        self.check()
        self.page_label.config(text=f'{self.page + 1} of {len(self.photos)}')

        if self.page == 0:
            self.btn_previous = tk.Button(self.label_frame, text='上一页',
                                          command=self.pre_page, state=tk.DISABLED).grid(row=2, column=1)

    def create_page(self):
        self.label_img = tk.Label(self.img_frame, image=self.photos[self.page])
        self.label_img.pack()

        self.check()

        self.page_label = tk.Label(self.label_frame, text='{} of {}'.format(
            1, len(self.photos)), font=('', 12), width=16, anchor=tk.CENTER)
        self.page_label.grid(row=1, column=1, columnspan=2)

        self.btn_previous = tk.Button(self.label_frame, text='上一页',
                                      command=self.pre_page, state=tk.DISABLED).grid(row=2, column=1)
        self.btn_next = tk.Button(self.label_frame, text='下一页',
                                  command=self.next_page).grid(row=2, column=2)

    def check(self):
        root_height = self.photos[self.page].height()
        root_width = self.photos[self.page].width()
        self.root.geometry(f"{root_width}x{root_height + 100}+100+100")
        self.root.update()


ImgViewer()
