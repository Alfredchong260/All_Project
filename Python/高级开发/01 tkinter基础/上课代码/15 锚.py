import tkinter as tk

root = tk.Tk()
root.geometry('500x300+100+100')

# label_1 = tk.Label(root, text="方位是 N",
#                    bg="green", width=20, height=5,
#                    font=('宋体', 18),
#                    # anchor='n', # 面向过程的写法
#                    # anchor=tk.N  # 面向对象的写法
#                    )
# # label_1.pack(side=tk.BOTTOM, anchor=tk.W)
# label_1.pack()

label_1 = tk.Label(root, text="方位是 N",
                   bg="green", width=20, height=5,
                   font=('宋体', 18),
                   # anchor='n', # 面向过程的写法
                   anchor=tk.NE  # 面向对象的写法
                   )
# label_1.pack(side=tk.BOTTOM, anchor=tk.W)
label_1.pack(side=tk.BOTTOM, anchor=tk.E)

root.mainloop()
