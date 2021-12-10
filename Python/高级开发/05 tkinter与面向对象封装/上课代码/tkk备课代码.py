import tkinter as tk
from tkinter import ttk

students = [{"name": "李四", "chinese": 50, "math": 40, "english": 30, "total": 120},
            {"name": "王五", "chinese": 100, "math": 100, "english": 100, "total": 300}]

root = tk.Tk()
root.geometry('500x300+100+100')

# 1. 创建字段
columns = ("name", "chinese", "math", "english")
columns_value = ('姓名', '语文', '数学', '英语')

# 2. 创建表格对象
tree_view = ttk.Treeview(root, show="headings", columns=columns)

# 3. 给表格添加字段名
tree_view.column('name', width=80, anchor='center')
tree_view.column('chinese', width=80, anchor='center')
tree_view.column('math', width=80, anchor='center')
tree_view.column('english', width=80, anchor='center')

# 4. 设置字段在页面上显示的内容
tree_view.heading('name', text='姓名')
tree_view.heading('chinese', text='语文')
tree_view.heading('math', text='数学')
tree_view.heading('english', text='英语')

# 5. 将表格对象布局到页面上
tree_view.pack(fill=tk.BOTH, expand=True)

# 6. 往表格中添加数据
for index, stu in enumerate(students):
    tree_view.insert('', index + 1, values=(stu['name'], str(stu['chinese']), str(stu['math']), str(stu['english'])))


def tree_view_click(event):
    # 7.1 遍历选中的元素
    for item in tree_view.selection():
        # 获取选中元素的值
        item_text = tree_view.item(item, "values")
        # 打印选中元素的值
        print(item_text)


# 7. 单击事件 获取当前点击行的值
# 鼠标左键抬起 点击触发事件 可以重复触发
tree_view.bind('<ButtonRelease-1>', tree_view_click)


# 鼠标选中一行回调
def select_tree(event):
    print(event)
    for item in tree_view.selection():
        item_text = tree_view.item(item, "values")
        print(item_text)


# 8. 选中行事件
tree_view.bind('<<TreeviewSelect>>', select_tree)


def del_select():
    for item in tree_view.selection():
        tree_view.delete(item)


# 9. 删除表格元素
del_btn = tk.Button(root, text='删除')
del_btn.pack()
# 9.2 配置删除事件
del_btn.config(command=del_select)

# 进入消息循环
root.mainloop()
