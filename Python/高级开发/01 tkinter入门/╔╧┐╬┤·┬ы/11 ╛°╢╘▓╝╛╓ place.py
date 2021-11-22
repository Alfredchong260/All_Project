import tkinter as tk

root = tk.Tk()
root.geometry('500x300+100+100')
font = ('宋体', 18)

tk.Label(root, text='', font=font,
         width=5, height=3).grid(row=0, column=0)
tk.Label(root, text='用户名:', font=font).grid(row=1, column=1, padx=10, pady=10)
tk.Entry(root, font=font).grid(row=1, column=2, padx=10, pady=10)
tk.Label(root, text='密 码:', font=font).grid(row=2, column=1, padx=10, pady=10)
tk.Entry(root, font=font).grid(row=2, column=2, padx=10, pady=10)

label = tk.Label(root, text='绝对布局')
# label.pack()
label.grid()

# relx 和 rely 选项指定的是相对于父组件的位置 小数百分比
# 范围是 00～1.0，因此 0.5 表示位于正中间。
# label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
"""
    pack 顺序布局
    grid 网格布局
    place 绝对布局 可以重叠带顺序与网格布局上面
"""
root.mainloop()
