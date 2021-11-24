import tkinter as tk

root = tk.Tk()
root.geometry('500x300+100+100')
font = ('宋体', 26)
bool_var = tk.BooleanVar()
# 如果需要默认选中
bool_var.set(True)
# 多选框 选中与未选中
check_button = tk.Checkbutton(root, text='测试一下', font=font, variable=bool_var)
check_button.pack()

button = tk.Button(root, text='获取多选框的值', font=font)
button.pack(side=tk.BOTTOM)


def click():
    print('多选框目前的状态:\t', bool_var.get())


button.config(command=click)
root.mainloop()
