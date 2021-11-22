"""
    作业提交格式
    + 使用源代码的方式提交，题目用 `注释` 的方式写在源代码里面。
    + 将所有代码放在同一个文件夹里面，然后弄成压缩包（不要分个提交）
    + 作业文件命名：期次（0111）-第几次作业（二位数）-学号-姓名.zip（例如0111-01-01000000-正心.zip）
      - 期次：0111（01为基础课程编号，10为基础第10期）
      - 第几次作业：第一次为 01，第二次为 02，依次递推
      - 每个学员都会有一个学号，所有作业提交都需要，没有学号请联系正心或者丸子老师。
    + 提交到QQ邮箱：2482749597@qq.com
    + 作业在第二次课课前讲解，答案与第二次课代码一起发放。
    + 写作业遇到问题请微信联系，写完之后再QQ邮箱提交。最迟提交时间为周三周日晚十点。
    + 【腾讯文档】进阶课作业统计（课程编码：0111）
https://docs.qq.com/sheet/DU2d0TW1ueVVqc3lS（学号查看）
"""
"""
    作业：使用表格布局，完成 计算器布局.png 的界面设计(grid)

灰色： #c6c6c6
橙色： #ffe1b5
"""
from tkinter import *

def button(text, bg, width, height, row, column, padx, pady, sticky=N, command=None):
    button1 = Button(root, text=text, font=font, bg=bg, width=width, height=height, command=command)
    button1.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)

root = Tk()
root.title('计算器')
# root.iconbitmap('icon.ico')
root.geometry('380x500+100+100')
root.config(background='white')
root.resizable(False, False)

font = ('', 20)

num_var = StringVar()

sep = Label(root, text='', height=2, bg='white', fg='white').grid(row=1, column=1)

main = Label(root, textvariable=num_var, font=font, anchor=E, width=6, bg='white').grid(row=2, column=3, padx=2, pady=5)

def num(number):
    if num_var.get() == '' or num_var.get() == '0':
        num_var.set(number)
    else:
        a = num_var.get()
        num_var.set(a + str(number))

def delete():
    old = num_var.get()
    length = len(old)
    new = old[0:length - 1]
    num_var.set(new)

def delet_all():
    num_var.set('0')

label_c = button('C', '#c6c6c6', 4, 2, 3, 1, 3, 3, command=delet_all)
label_arrow = button('<-', '#c6c6c6', 4, 2, 3, 2, 3, 3, command=delete)
label_divide = button('/', '#c6c6c6', 4, 2, 3, 3, 3, 3, command=lambda x = '/': num(x))
label_times = button('X', '#c6c6c6', 4, 2, 3, 4, 3, 3, command=lambda x = 'X': num(x))

label_7 = button('7', '#ffe1b5', 4, 2, 4, 1, 3, 3, command=lambda x = 7: num(x))
label_8 = button('8', '#ffe1b5', 4, 2, 4, 2, 3, 3, command=lambda x = 8: num(x))
label_9 = button('9', '#ffe1b5', 4, 2, 4, 3, 3, 3, command=lambda x = 9: num(x))
label_minus = button('-', '#c6c6c6', 4, 2, 4, 4, 3, 3, command=lambda x = '-': num(x))

label_4 = button('4', '#ffe1b5', 4, 2, 5, 1, 3, 3, command=lambda x = 4: num(x))
label_5 = button('5', '#ffe1b5', 4, 2, 5, 2, 3, 3, command=lambda x = 5: num(x))
label_6 = button('6', '#ffe1b5', 4, 2, 5, 3, 3, 3, command=lambda x = 6: num(x))
label_plus = button('+', '#c6c6c6', 4, 2, 5, 4, 3, 3, sticky=N, command=lambda x = '+': num(x))

label_1 = button('1', '#ffe1b5', 4, 2, 6, 1, 3, 3, command=lambda x = 1: num(x))
label_2 = button('2', '#ffe1b5', 4, 2, 6, 2, 3, 3, command=lambda x = 2: num(x))
label_3 = button('3', '#ffe1b5', 4, 2, 6, 3, 3, 3, command=lambda x = 3: num(x))
label_equal = button('=', '#c6c6c6', 4, 5, 6, 4, 3, 3)

label_0 = Button(root, text='0', font=font, bg='#ffe1b5', width=10, height=2, command=lambda x = 0: num(x)).place(relx=0.01, rely=0.834)
label_dot = Button(root, text='.', font=font, bg='#ffe1b5', width=4, height=2, command=lambda x = '.': num(x)).place(relx=0.505, rely=0.834)

root.mainloop()
