# 导入模块，取别名
import tkinter as tk

# 实例化一个窗体对象
root = tk.Tk()
# 设置窗口的大小长宽为300x300出现的位置距离窗口左上角+150+150
root.geometry("295x280+150+150")
root.title('计算器')
root.attributes("-alpha", 0.9)
root["background"] = "#ffffff"

# 先定义一个列表收集输入的内容
lists = []
result_num = tk.StringVar()
result_num.set(0)

lable1 = tk.Label(root,
                  textvariable=result_num, width=20, height=2,
                  font=('宋体', 20), justify='left',
                  background='#ffffff', anchor='se')

lable1.grid(padx=4, pady=4, row=0, column=0, columnspan=4)

button_clear = tk.Button(root, text='C', width=5, font=('宋体', 16), relief='flat', background='#C0C0C0')
button_back = tk.Button(root, text='←', width=5, font=('宋体', 16), relief='flat', background='#C0C0C0')
button_division = tk.Button(root, text='/', width=5, font=('宋体', 16), relief='flat', background='#C0C0C0')
button_multiplication = tk.Button(root, text='x', width=5, font=('宋体', 16), relief='flat', background='#C0C0C0')

button_clear.grid(padx=4, pady=2, row=1, column=0)
button_back.grid(padx=4, pady=2, row=1, column=1)
button_division.grid(padx=4, pady=2, row=1, column=2)
button_multiplication.grid(padx=4, pady=2, row=1, column=3)

button_seven = tk.Button(root, text='7', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD')
button_eight = tk.Button(root, text='8', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD')
button_nine = tk.Button(root, text='9', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD')
button_subtraction = tk.Button(root, text='—', width=5, font=('宋体', 16), relief='flat', background='#C0C0C0')

button_seven.grid(padx=4, pady=2, row=2, column=0)
button_eight.grid(padx=4, pady=2, row=2, column=1)
button_nine.grid(padx=4, pady=2, row=2, column=2)
button_subtraction.grid(padx=4, pady=2, row=2, column=3)

button_four = tk.Button(root, text='4', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD')
button_five = tk.Button(root, text='5', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD')
button_six = tk.Button(root, text='6', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD')
button_addition = tk.Button(root, text='+', width=5, font=('宋体', 16), relief='flat', background='#C0C0C0')

button_four.grid(padx=4, pady=2, row=3, column=0)
button_five.grid(padx=4, pady=2, row=3, column=1)
button_six.grid(padx=4, pady=2, row=3, column=2)
button_addition.grid(padx=4, pady=2, row=3, column=3)

button_one = tk.Button(root, text='1', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD')
button_two = tk.Button(root, text='2', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD')
button_three = tk.Button(root, text='3', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD')
button_equal = tk.Button(root, text='=', width=5, height=3, font=('宋体', 16), relief='flat', background='#C0C0C0')

button_one.grid(padx=4, pady=2, row=4, column=0)
button_two.grid(padx=4, pady=2, row=4, column=1)
button_three.grid(padx=4, pady=2, row=4, column=2)
button_equal.grid(padx=4, pady=2, row=4, rowspan=2, column=3)

button_zero = tk.Button(root, text='0', width=12, font=('宋体', 16), relief='flat', background='#FFDEAD')
button_decimal = tk.Button(root, text='.', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD')

button_zero.grid(padx=4, pady=4, row=5, column=0, columnspan=2)
button_decimal.grid(padx=4, row=5, column=2)


def append_num(i):
    lists.append(i)
    result_num.set(''.join(lists))


def operator(i):
    # 如果列表大于零
    if len(lists) > 0:
        # 如果列表最后的字符为运算符
        # 修改运算符的符号
        if lists[-1] in ['+', '-', '*', '/']:
            # 更换最后一个内容的运算符
            lists[-1] = i
        # 如果之前列表的最后一个数字为字符串，则记录运算符
        else:
            lists.append(i)
        # 设置屏幕上显示的内容
        result_num.set(''.join(lists))


def equal():
    a = ''.join(lists)
    end_num = eval(a)
    result_num.set(end_num)
    lists.clear()
    lists.append(str(end_num))


def clear():
    lists.clear()
    result_num.set(0)


def back():
    del lists[-1]
    result_num.set(lists)


button_clear.config(command=clear)
button_back.config(command=back)
button_division.config(command=lambda: operator('/'))
button_multiplication.config(command=lambda: operator('*'))

button_seven.config(command=lambda: append_num('7'))
button_eight.config(command=lambda: append_num('8'))
button_nine.config(command=lambda: append_num('9'))
button_subtraction.config(command=lambda: operator('-'))

button_four.config(command=lambda: append_num('4'))
button_five.config(command=lambda: append_num('5'))
button_six.config(command=lambda: append_num('6'))
button_addition.config(command=lambda: operator('+'))

button_one.config(command=lambda: append_num('1'))
button_two.config(command=lambda: append_num('2'))
button_three.config(command=lambda: append_num('3'))
button_equal.config(command=equal)

button_zero.config(command=lambda: append_num('0'))
button_decimal.config(command=lambda: append_num('.'))

# 进入消息循环，显示窗口
root.mainloop()
