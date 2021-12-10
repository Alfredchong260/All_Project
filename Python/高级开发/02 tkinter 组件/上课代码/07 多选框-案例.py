import tkinter as tk

root = tk.Tk()
root.geometry('500x300+100+100')
font = ('宋体', 26)

girls = ['西施', '王昭君', '貂蝉', '杨玉环']
var_list = [tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()]
for index in range(len(var_list)):
    tk.Checkbutton(root, text=girls[index], font=font, variable=var_list[index]).pack(anchor=tk.W)

button = tk.Button(root, text='获取多选框的值', font=font)
button.pack(side=tk.BOTTOM)


def click():
    # print('多选框目前的状态:\t', var_list)  # 列表里面的元素每一个进行遍历
    # result = []
    # for index in range(len(var_list)):
    #     # 如果当前的多选框选中了内容
    #     if var_list[index].get():
    #         result.append(girls[index])
    # print(result)
    print('多选框目前的状态:\t', [girls[index] for index in range(len(var_list)) if var_list[index].get()])


button.config(command=click)
root.mainloop()
