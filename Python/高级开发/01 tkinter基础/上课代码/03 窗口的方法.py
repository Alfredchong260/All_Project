import tkinter as tk

root = tk.Tk()
root.title('窗口的基本属性')
root.geometry('500x300+100+100')
# 获取屏幕大小
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print('屏幕的大小:', screen_width, screen_height)
# 就相当于在 word 里面写东西
root.update()  # 更新一下窗口,才会有窗口的属性
# 获取窗体的大小
winfo_height = root.winfo_height()
winfo_width = root.winfo_width()
print('窗体的大小', winfo_width, winfo_height)
# 获取窗体的位置
winfo_x = root.winfo_x()
winfo_y = root.winfo_y()
print('窗体的位置', winfo_x, winfo_y)
# 单位是像素
root.mainloop()
