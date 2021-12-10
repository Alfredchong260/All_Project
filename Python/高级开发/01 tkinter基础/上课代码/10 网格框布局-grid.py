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
# 没有第三行,后面的就会上移
tk.Button(root, text='提交', font=font, width=20).grid(row=4, column=2, padx=10, pady=10)
root.mainloop()
