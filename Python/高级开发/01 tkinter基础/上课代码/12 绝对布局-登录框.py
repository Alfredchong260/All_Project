import tkinter as tk

root = tk.Tk()
root.geometry('500x300+100+100')
font = ('宋体', 18)

tk.Label(root, text='用户名:', font=font).place(relx=0.2, rely=0.2)
tk.Entry(root, font=font).place(relx=0.4, rely=0.2)
tk.Label(root, text='密 码:', font=font).place(relx=0.2, rely=0.4)
tk.Entry(root, font=font).place(relx=0.4, rely=0.4)
tk.Button(root, text='提交', font=font, width=20).place(relx=0.4, rely=0.6)
root.mainloop()
