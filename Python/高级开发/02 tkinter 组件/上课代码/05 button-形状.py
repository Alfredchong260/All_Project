import tkinter as tk

root = tk.Tk()
root.geometry("500x300+100+100")
# 笔型
button1 = tk.Button(root, text="笔型", cursor="pencil")
button1.pack()

# 圆形
button2 = tk.Button(root, text="圆形", cursor="circle")
button2.pack()

# 手型1
button3 = tk.Button(root, text="手型1", cursor="hand1")
button3.pack()

# 手型2
button4 = tk.Button(root, text="手型2", cursor="hand2")
button4.pack()

root.mainloop()
