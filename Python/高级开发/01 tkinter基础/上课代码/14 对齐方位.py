import tkinter as tk

root = tk.Tk()
root.geometry('500x300+100+100')

tk.Label(root, text='右 Right', bg='#1d953f', font=('宋体', 18),
         width=20, height=5).pack(
    side=tk.TOP,  # side: 控制位置 在页面中的上下左右
    anchor=tk.S  # anchor: 锚
)
"""
    side: 控制位置 在页面中的上下左右
    anchor: 在位置对齐之后,调整内容的方位(上下左右东南西北)
"""

root.mainloop()
