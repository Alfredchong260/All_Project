import tkinter as tk

root = tk.Tk()
root.geometry('500x300+100+100')
font = ('宋体', 26)

# 1. 定义可变变量的值
radio_var_str = tk.StringVar()
# radio_var_str.set('其他')
# 2. 创建单选框组件
# 修改了单选框返回的值,那个地方需要进行变动
# variable 同一组单选框必须指定同一个可变变量
# value 当对象的单选框选中之后, value 的值会被赋值给 variable
tk.Radiobutton(root, text='男', font=font, variable=radio_var_str, value='男').pack(anchor=tk.W)
tk.Radiobutton(root, text='女', font=font, variable=radio_var_str, value='女').pack(anchor=tk.W)
tk.Radiobutton(root, text='其他', font=font, variable=radio_var_str, value='其他').pack(anchor=tk.W)

button = tk.Button(root, text='获取多选框的值', font=font)
button.pack(side=tk.BOTTOM)


def click():
    print('单选框目前的状态:\t',radio_var_str.get())


button.config(command=click)
root.mainloop()
