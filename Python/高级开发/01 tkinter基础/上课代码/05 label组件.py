import tkinter as tk

root = tk.Tk()
root.title('label组件')
root.geometry('500x300+100+100')
label = tk.Label(root,
                 text='学 python 就先学 tkinter',  # 设置文字属性
                 font=('宋体', 24),  # 设置字体
                 fg='red',
                 bg='#263238',  # 颜色可以给十六进制的
                 # height=3,
                 width=200,
                 pady=10,  # padding y
                 )
# ctrl + alt + l (qq/网易云 热键冲突)
label.pack()

label2 = tk.Label(root,
                  text='学 python 就先学 tkinter',  # 设置文字属性
                  font=('宋体', 24),  # 设置字体
                  bd=5,
                  )
label2.pack()
root.mainloop()
