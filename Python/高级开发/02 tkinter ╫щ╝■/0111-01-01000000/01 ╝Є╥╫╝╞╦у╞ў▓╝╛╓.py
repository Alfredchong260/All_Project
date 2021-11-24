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
import tkinter as tk

root = tk.Tk()
root.title('计算器')
root.geometry('295x280+150+150')
root['background'] = '#ffffff'
label = tk.Label(root,
                 width=20, height=2,
                 text='0', font=('宋体', 20),
                 anchor=tk.SE
                 )
label.grid(row=1, column=1, columnspan=4)

button_clear = tk.Button(root, text='C', width=5, font=('宋体', 16), bg='#c6c6c6', relief=tk.FLAT)
button_back = tk.Button(root, text='←', width=5, font=('宋体', 16), bg='#c6c6c6', relief=tk.FLAT)
button_division = tk.Button(root, text='/', width=5, font=('宋体', 16), bg='#c6c6c6', relief=tk.FLAT)
button_mul = tk.Button(root, text='X', width=5, font=('宋体', 16), bg='#c6c6c6', relief=tk.FLAT)
button_clear.grid(row=2, column=1, padx=4, pady=2)
button_back.grid(row=2, column=2, padx=4, pady=2)
button_division.grid(row=2, column=3, padx=4, pady=2)
button_mul.grid(row=2, column=4, padx=4, pady=2)

button_seven = tk.Button(root, text='7', width=5, font=('宋体', 16), bg='#ffe1b5', relief=tk.FLAT)
button_eight = tk.Button(root, text='8', width=5, font=('宋体', 16), bg='#ffe1b5', relief=tk.FLAT)
button_nigh = tk.Button(root, text='9', width=5, font=('宋体', 16), bg='#ffe1b5', relief=tk.FLAT)
button_sub = tk.Button(root, text='-', width=5, font=('宋体', 16), bg='#c6c6c6', relief=tk.FLAT)
button_seven.grid(row=3, column=1, padx=4, pady=2)
button_eight.grid(row=3, column=2, padx=4, pady=2)
button_nigh.grid(row=3, column=3, padx=4, pady=2)
button_sub.grid(row=3, column=4, padx=4, pady=2)

button_four = tk.Button(root, text='4', width=5, font=('宋体', 16), bg='#ffe1b5', relief=tk.FLAT)
button_five = tk.Button(root, text='5', width=5, font=('宋体', 16), bg='#ffe1b5', relief=tk.FLAT)
button_six = tk.Button(root, text='6', width=5, font=('宋体', 16), bg='#ffe1b5', relief=tk.FLAT)
button_add = tk.Button(root, text='+', width=5, font=('宋体', 16), bg='#c6c6c6', relief=tk.FLAT)
button_four.grid(row=4, column=1, padx=4, pady=2)
button_five.grid(row=4, column=2, padx=4, pady=2)
button_six.grid(row=4, column=3, padx=4, pady=2)
button_add.grid(row=4, column=4, padx=4, pady=2)

button_onr = tk.Button(root, text='1', width=5, font=('宋体', 16), bg='#ffe1b5', relief=tk.FLAT)
button_two = tk.Button(root, text='2', width=5, font=('宋体', 16), bg='#ffe1b5', relief=tk.FLAT)
button_three = tk.Button(root, text='3', width=5, font=('宋体', 16), bg='#ffe1b5', relief=tk.FLAT)
button_equal = tk.Button(root, text='=', width=5, height=3, font=('宋体', 16), bg='#c6c6c6', relief=tk.FLAT)
button_onr.grid(row=5, column=1, padx=4, pady=2)
button_two.grid(row=5, column=2, padx=4, pady=2)
button_three.grid(row=5, column=3, padx=4, pady=2)
button_equal.grid(row=5, column=4, padx=4, pady=2, rowspan=2)

button_zero1 = tk.Button(root, text='0', width=12, font=('宋体', 16), bg='#ffe1b5', relief=tk.FLAT)
# button_zero2 = tk.Button(root, text='0', width=5, font=('宋体', 16), bg='#ffe1b5')
button_dot = tk.Button(root, text='.', width=5, font=('宋体', 16), bg='#ffe1b5', relief=tk.FLAT)

# button_equal2 = tk.Button(root, text='=', width=5, font=('宋体', 16), bg='#c6c6c6')
button_zero1.grid(row=6, column=1, padx=4, pady=2, columnspan=2)
# button_zero2.grid(row=6, column=2, padx=4, pady=2)
button_dot.grid(row=6, column=3, padx=4, pady=2)
# button_equal2.grid(row=6, column=4, padx=4, pady=2)

# 竖行模式 alt + shift + 光标拖动
# 批量选择  ctrl + shift + ->
root.mainloop()
