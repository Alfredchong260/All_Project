#  导入模块，取别名
import tkinter as tk

#  实例化一个窗体对象
root = tk.Tk()
root.geometry('500x300+100+100')
#  导入图片
img1 = tk.PhotoImage(file="logo.png")
#  在标签里放入图片
label_image1 = tk.Label(root, image=img1)
label_image1.pack()
#  进入消息循环，显示窗口
root.mainloop()
