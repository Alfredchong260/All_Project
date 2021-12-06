"""
    图片已经加载好了，请参考 `图片查看器.png` 实现图片查看器的逻辑
"""

import tkinter as tk
import glob

from PIL import Image, ImageTk

# 记录当前显示第几张图片
current_photo_no = 0

root = tk.Tk()
# 加载本地图片
photos = glob.glob('photo/*.jpg')
photos = [ImageTk.PhotoImage(Image.open(file)) for file in photos]

"""在下面实现代码"""
number_str_var = tk.StringVar()
number_str_var.set('1 of 4')

photo_label = tk.Label(root, image=photos[current_photo_no], width=900, height=600)
photo_label.pack()

#  sunken 沉没的
label_2 = tk.Label(root, textvariable=number_str_var, relief=tk.SUNKEN, bd=1)
label_2.pack(fill=tk.X)

button_frame = tk.Frame(root)
button_frame.pack(anchor=tk.CENTER)

prev_photo = tk.Button(button_frame, text='上一页')
next_photo = tk.Button(button_frame, text='下一页')

prev_photo.pack(side=tk.LEFT)
next_photo.pack(side=tk.LEFT)


def next_photo_event():
    global current_photo_no
    # 0-3   4
    if current_photo_no < len(photos) - 1:
        current_photo_no += 1
    number_str_var.set(f'{current_photo_no + 1} of {len(photos)}')
    photo_label.config(image=photos[current_photo_no])


def prev_photo_event():
    global current_photo_no
    # 0-3   4
    if current_photo_no > 0:
        current_photo_no -= 1
    number_str_var.set(f'{current_photo_no + 1} of {len(photos)}')
    photo_label.config(image=photos[current_photo_no])


def photo_event(next_no):
    global current_photo_no
    # 0-3   4
    current_photo_no += next_no
    if current_photo_no < 0:
        current_photo_no = 0
    if current_photo_no >= len(photos):
        current_photo_no = len(photos) - 1
    number_str_var.set(f'{current_photo_no + 1} of {len(photos)}')
    photo_label.config(image=photos[current_photo_no])


"""绑定事件"""
# next_photo.config(command=next_photo_event)
# prev_photo.config(command=prev_photo_event)
next_photo.config(command=lambda: photo_event(1))
prev_photo.config(command=lambda: photo_event(-1))
root.mainloop()
