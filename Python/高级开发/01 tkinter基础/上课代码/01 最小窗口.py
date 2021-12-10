import tkinter  # 内置库,不需要进行安装

# 1. 创建一个窗口对象
root = tkinter.Tk()
# 1.1 设置标题内容
root.title('第一个桌面程序')
# 1.2 设置窗口的大小 宽度 x 高度 + 左上角的x距离 + 左上角的y距离
root.geometry('500x300+100+100')

# 2 创建一个 label 组件
label = tkinter.Label(root, text='我是第一个label组件')
label.pack()  # 在页面中显示出来

# 事件死循环,显示窗口
root.mainloop()

"""
    在使用别人的工具时,不要纠结为什么这样用
    
    在设计这个工具的时候随便命名的,之后所有的程序员都是这样使用,所以就传递下来了
"""