import tkinter as tk

root = tk.Tk()
root.geometry('500x300+100+100')
font = ('宋体', 26)
# 二值形的列表
langs = [
    ('python', 1),
    ('perl', 2),
    ('ruby', 3),
    ('lua', 4),
]

int_var = tk.IntVar()
tk.Label(root, text='请选择你最喜欢的一门语言')
for item in langs:
    tk.Radiobutton(root, value=item[1], text=item[0], variable=int_var).pack()

button = tk.Button(root, text='确定', font=font)
button.pack(side=tk.BOTTOM)


def click():
    result_int = int_var.get()  # 获取的单选框选中的值
    for item in langs:
        #
        if item[1] == result_int:
            print('选中的结果:\t', item[0])


button.config(command=click)
root.mainloop()
