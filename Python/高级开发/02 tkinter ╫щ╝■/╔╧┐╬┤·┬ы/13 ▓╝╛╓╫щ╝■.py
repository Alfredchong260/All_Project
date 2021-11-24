import tkinter as tk

root = tk.Tk()
root.geometry('500x300+100+100')
font = ('宋体', 16)

# 布局组件实现嵌套布局
# tk.Label(root, bg='red', width=10, height=2).pack(side=tk.LEFT)
# tk.Label(root, bg='blue', width=10, height=2).pack(side=tk.LEFT)
# tk.Label(root, bg='yellow', width=10, height=2).pack(side=tk.LEFT)

# 左边的布局容器
# 布局容器默认是没有宽高的

# LabelFrame 会多一个框线,多一个文章
left_frame = tk.LabelFrame(root, text='布局容器', width=250, height=200, bg='pink')
left_frame.pack(side=tk.LEFT)  # 容器是从左到右

# 容器里面的元素时从上到下
tk.Label(left_frame, bg='red', width=10, height=2).pack()
tk.Label(left_frame, bg='blue', width=10, height=2).pack()
tk.Label(left_frame, bg='yellow', width=10, height=2).pack()


# 布局容器默认是没有宽高的
# right_frame = tk.Frame(root, width=250, height=200, bg='pink')
# right_frame.pack(side=tk.RIGHT, fill=tk.Y)  # 容器是从左到右

# # 容器里面的元素时从上到下
# tk.Label(right_frame, bg='red', width=10).pack(side=tk.LEFT, fill=tk.Y)
# tk.Label(right_frame, bg='blue', width=10).pack(side=tk.LEFT, fill=tk.Y)
# tk.Label(right_frame, bg='yellow', width=10).pack(side=tk.LEFT, fill=tk.Y)

root.mainloop()
