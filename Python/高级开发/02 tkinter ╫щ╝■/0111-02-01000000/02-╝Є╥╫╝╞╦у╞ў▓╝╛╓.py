""""""
"""
    选做：尝试自己完成简易计算器的逻辑（能实现多少实现多少）
    
    1. 点击数字与运算符号之后将内容添加到一个列表
        1.1 将列表的元素合并为字符串，设置到最上面的label组件中显示
        
    2. 点击等于号之后，将列表的内容合并为字符串 使用eval 进行计算，将结果显示到页面中
        2.1 eval 是将字符串当做python里面的代码使用,参考下面案例
            >>> eval('1+2+3*5')
            >>> 18
    3. 点击删除符号，将列表的最后一个元素删除
    4. 计算时重复点击运算符号可以覆盖（先点加再点减最终用减进行计算）

"""
from tkinter import *

def button(text, bg, width, height, row, column, padx, pady, sticky=N, command=None, rowspan=1, columnspan=1):
    button1 = Button(root, text=text, font=font, bg=bg,
                     width=width, height=height, command=command, relief=SUNKEN)
    button1.grid(row=row, column=column, padx=padx, pady=pady,
                 sticky=sticky, rowspan=rowspan, columnspan=columnspan)

result_lst = []

root = Tk()
root.title('计算器')
# root.iconbitmap('icon.ico')
root.geometry('380x500+100+100')
root.config(background='white')
root.resizable(False, False)

font = ('', 20)

num_var = StringVar()
num_var.set('0')

sep = Label(root, text='', height=2, bg='white',
            fg='white').grid(row=1, column=1)

main = Label(root, textvariable=num_var, font=font, anchor=E,
             width=23, bg='white').grid(row=2, column=1, columnspan=8)

def add_num(num):
    operator = ['+', '-', '*', '/', '.']
    if num in operator and result_lst[-1] in operator:
        result_lst[-1] = num
        num_var.set(''.join(result_lst))
    else:
        result_lst.append(num)
        num_var.set(''.join(result_lst))

def delete_all():
    result_lst.clear()
    num_var.set('0')

def delete_one():
    result_lst.pop(-1)
    num_var.set(''.join(result_lst))

def calculate():
    cal_str = ''.join(result_lst)
    ans = eval(cal_str)
    result_lst.clear()
    result_lst.append(str(ans))
    num_var.set(ans)

label_c = button('C', '#c6c6c6', 4, 2, 3, 1, 3, 3, command=delete_all)
label_arrow = button('←', '#c6c6c6', 4, 2, 3, 2, 3, 3, command=delete_one)
label_divide = button('/', '#c6c6c6', 4, 2, 3, 3, 3, 3, command=lambda:add_num('/'))
label_times = button('*', '#c6c6c6', 4, 2, 3, 4, 3, 3, command=lambda:add_num('*'))

label_7 = button('7', '#ffe1b5', 4, 2, 4, 1, 3, 3, command=lambda:add_num('7'))
label_8 = button('8', '#ffe1b5', 4, 2, 4, 2, 3, 3, command=lambda:add_num('8'))
label_9 = button('9', '#ffe1b5', 4, 2, 4, 3, 3, 3, command=lambda:add_num('9'))
label_minus = button('-', '#c6c6c6', 4, 2, 4, 4, 3, 3, command=lambda:add_num('-'))

label_4 = button('4', '#ffe1b5', 4, 2, 5, 1, 3, 3, command=lambda:add_num('4'))
label_5 = button('5', '#ffe1b5', 4, 2, 5, 2, 3, 3, command=lambda:add_num('5'))
label_6 = button('6', '#ffe1b5', 4, 2, 5, 3, 3, 3, command=lambda:add_num('6'))
label_plus = button('+', '#c6c6c6', 4, 2, 5, 4, 3, 3, sticky=N, command=lambda:add_num('+'))

label_1 = button('1', '#ffe1b5', 4, 2, 6, 1, 3, 3, command=lambda:add_num('1'))
label_2 = button('2', '#ffe1b5', 4, 2, 6, 2, 3, 3, command=lambda:add_num('2'))
label_3 = button('3', '#ffe1b5', 4, 2, 6, 3, 3, 3, command=lambda:add_num('3'))
label_equal = button('=', '#c6c6c6', 4, 5, 6, 4, 3, 3, rowspan=2, command=calculate)

label_0 = button('0', '#ffe1b5', 10, 2, 7, 1, 3, 3, columnspan=2, command=lambda:add_num('0'))
label_dot = button('.', '#ffe1b5', 4, 2, 7, 3, 3, 3, command=lambda:add_num('.'))

root.mainloop()

