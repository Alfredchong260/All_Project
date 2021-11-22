import tkinter as tk

root = tk.Tk()
root.title('窗口的基本属性')
root.geometry('500x300+100+100')

#  设置背景色，可以用英文名，也可以用十六进制表示的颜色。
# root["background"] = "#00ffff"
#  如果需要定制图标,就必须给ico格式的
root.iconbitmap('icon.ico')  # ico png jpg jpeg psd ......

# #  True 全屏；False 正常显示
# root.attributes("-fullscreen", True)
root.mainloop()
