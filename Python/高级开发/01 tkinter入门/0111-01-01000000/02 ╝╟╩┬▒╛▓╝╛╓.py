"""
完成 记事本布局.png （pack）


侧边栏颜色：#faebd7
底部栏颜色：#f0f0f0
中间区域颜色：#ffffff

拖拽滚动栏暂时可以不写

"""

from tkinter import *

root = Tk()
root.geometry('400x300')
root.title('04 记事本')
root.config(bg='#ffffff')

label_down = Label(root, text='字符数：0', bg='#f0f0f0', height=1).pack(side=BOTTOM, fill=X)
label_side = Label(root, bg='#faebd7', width=2).pack(side=LEFT, fill=Y)
text1 = Text(label_down)

root.mainloop()
