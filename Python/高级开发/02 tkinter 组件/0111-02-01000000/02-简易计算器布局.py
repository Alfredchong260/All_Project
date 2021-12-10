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
import tkinter as tk

# 实例化一个窗体对象
root = tk.Tk()
# 设置窗口的大小长宽为300x300出现的位置距离窗口左上角+150+150
root.geometry("295x280+150+150")
root.title('计算器')
# root.attributes("-alpha", 0.9)
root["background"] = "#ffffff"

lable1 = tk.Label(root,
                  width=20, height=2,
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

# 倒数第二行
button_one = tk.Button(root, text='1', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD')
button_two = tk.Button(root, text='2', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD')
button_three = tk.Button(root, text='3', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD')
button_equal = tk.Button(root, text='=', width=5, height=3, font=('宋体', 16), relief='flat', background='#C0C0C0')


button_one.grid(padx=4, pady=2, row=4, column=0)
button_two.grid(padx=4, pady=2, row=4, column=1)
button_three.grid(padx=4, pady=2, row=4, column=2)
# 等于号实现跨列操作
button_equal.grid(padx=4, pady=2, row=4, rowspan=2, column=3)

# 最后一行
button_zero = tk.Button(root, text='0', width=12, font=('宋体', 16), relief='flat', background='#FFDEAD')
button_decimal = tk.Button(root, text='.', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD')
# 0 实现跨行操作
button_zero.grid(padx=4, pady=4, row=5, column=0, columnspan=2)
button_decimal.grid(padx=4, row=5, column=2)

# 进入消息循环，显示窗口
root.mainloop()
